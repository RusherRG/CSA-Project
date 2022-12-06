from instruction.states import (
    InstructionFetchState,
    InstructionDecodeState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)

MemSize = 1000  # memory size, in reality, the memory size should be 2^32, but for this lab, for the space resaon, we keep it as this large number, but the memory is still 32-bit addressable.


class InsMem(object):
    def __init__(self, name: str, io_dir: str):
        self.id = name

        with open(io_dir + "/imem.txt", "r") as im:
            self.IMem = [data.replace("\n", "") for data in im.readlines()]

    def read_instr(self, read_address: int) -> str:
        # read instruction memory
        # return 32 bit hex val
        return "".join(self.IMem[read_address : read_address + 4])


class DataMem(object):
    def __init__(self, name: str, io_dir: str):
        self.id = name
        self.io_dir = io_dir
        with open(io_dir + "/dmem.txt", "r") as dm:
            self.DMem = [data.replace("\n", "") for data in dm.readlines()]
        self.DMem.extend(["00000000"] * (MemSize - len(self.DMem)))

    def read_data_mem(self, read_addr: str) -> str:
        # read data memory
        # return 32 bit hex val
        read_addr_int = bin2int(read_addr)
        return "".join(self.DMem[read_addr_int : read_addr_int + 4])

    def write_data_mem(self, addr: str, write_data: str):
        # write data into byte addressable memory
        addr_int = bin2int(addr)
        for i in range(4):
            self.DMem[addr_int + i] = write_data[8 * i : 8 * (i + 1)]

    def output_data_mem(self):
        resPath = self.io_dir + "/output/" + self.id + "_DMEMResult.txt"
        with open(resPath, "w") as rp:
            rp.writelines([str(data) + "\n" for data in self.DMem])


class RegisterFile(object):
    def __init__(self, io_dir):
        self.output_file = io_dir + "RFResult.txt"
        self.registers = [int2bin(0) for _ in range(32)]

    def read_RF(self, reg_addr: str) -> str:
        # Fill in
        return self.registers[bin2int(reg_addr)]

    def write_RF(self, reg_addr: str, wrt_reg_data: str):
        # Fill in
        if reg_addr == "00000":
            return
        self.registers[bin2int(reg_addr)] = wrt_reg_data

    def output_RF(self, cycle):
        op = ["-" * 70 + "\n", "State of RF after executing cycle:" + str(cycle) + "\n"]
        op.extend([f"{val}" + "\n" for val in self.registers])
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

    def next(self):
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


def int2bin(x: int, n_bits: int = 32) -> str:
    bin_x = bin(x & (2**n_bits - 1))[2:]
    return "0" * (n_bits - len(bin_x)) + bin_x


def bin2int(x: str, sign_ext: bool = False) -> int:
    if sign_ext and x[0] == "1":
        return -(-int(x, 2) & (2 ** len(x) - 1))
    return int(x, 2)
