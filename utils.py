from instruction.states import (
    InstructionFetchState,
    InstructionDecodeState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)


class InsMem(object):
    def __init__(self, name: str, io_dir: str):
        self.id = name

        with open(io_dir + "/imem.txt") as im:
            self.IMem = [data.replace("\n", "") for data in im.readlines()]

    def read_instr(self, read_address: int) -> str:
        # read instruction memory
        # return 32 bit hex val
        return "".join(self.IMem[read_address : read_address + 4])


class DataMem(object):
    def __init__(self, name: str, io_dir: str):
        self.id = name
        self.io_dir = io_dir
        with open(io_dir + "/dmem.txt") as dm:
            self.DMem = [data.replace("\n", "") for data in dm.readlines()]

    def read_data_mem(self, read_addr):
        # read data memory
        # return 32 bit hex val
        return self.DMem[read_addr : read_addr + 4]

    def write_data_mem(self, addr, write_data):
        # write data into byte addressable memory
        write_data_bin = bin(write_data)[2:]
        write_data_bin = (32 - len(write_data_bin)) * "0" + write_data_bin
        for i in range(4):
            self.DMem[addr + i] = write_data_bin[8 * i : 8 * (i + 1)]

    def output_data_mem(self):
        resPath = self.io_dir + "/" + self.id + "_DMEMResult.txt"
        with open(resPath, "w") as rp:
            rp.writelines([str(data) + "\n" for data in self.DMem])


class RegisterFile(object):
    def __init__(self, io_dir):
        self.output_file = io_dir + "RFResult.txt"
        self.registers = [0x0 for i in range(32)]

    def read_RF(self, reg_addr):
        # Fill in
        return self.registers[reg_addr]

    def write_RF(self, reg_addr, wrt_reg_data):
        # Fill in
        self.registers[reg_addr] = wrt_reg_data

    def output_RF(self, cycle):
        op = ["-" * 70 + "\n", "State of RF after executing cycle:" + str(cycle) + "\n"]
        op.extend([str(val) + "\n" for val in self.registers])
        if cycle == 0:
            perm = "w"
        else:
            perm = "a"
        with open(self.output_file, perm) as file:
            file.writelines(op)


class State(object):
    def __init__(self):
        self.IF = InstructionFetchState()
        self.ID = InstructionDecodeState()
        self.EX = ExecutionState()
        self.MEM = MemoryAccessState()
        self.WB = WriteBackState()


class Core(object):
    def __init__(self, io_dir, imem, dmem):
        self.myRF = RegisterFile(io_dir)
        self.cycle = 0
        self.halted = False
        self.io_dir = io_dir
        self.state = State()
        self.nextState = State()
        self.ext_imem = imem
        self.ext_dmem = dmem
