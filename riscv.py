import os
import argparse

from instruction import InstructionSet
from utils import DataMem, InsMem, Core, State

MemSize = 1000  # memory size, in reality, the memory size should be 2^32, but for this lab, for the space resaon, we keep it as this large number, but the memory is still 32-bit addressable.


class SingleStageCore(Core):
    def __init__(self, io_dir, imem, dmem):
        super(SingleStageCore, self).__init__(io_dir + "/output/SS_", imem, dmem)
        self.opFilePath = io_dir + "/output/StateResult_SS.txt"

    def step(self):
        # Your implementation
        new_instr = self.ext_imem.read_instr(self.state.IF.PC)[::-1]
        self.state.ID.instr = new_instr
        instr = InstructionSet().decode(new_instr)
        print(instr)
        instr.run(self.state, self.myRF, self.ext_dmem)
        if self.state.IF.nop:
            self.halted = True
        else:
            self.state.IF.PC += 4

        self.myRF.output_RF(self.cycle)  # dump RF
        self.print_state(
            self.state, self.cycle
        )  # print states after executing cycle 0, cycle 1, cycle 2 ...

        self.state.next()  # The end of the cycle and updates the current state with the values calculated in this cycle
        self.cycle += 1

    def print_state(self, state, cycle):
        printstate = [
            "-" * 70 + "\n",
            "State after executing cycle: " + str(cycle) + "\n",
        ]
        printstate.append("IF.PC: " + str(state.IF.PC) + "\n")
        printstate.append("IF.nop: " + str(state.IF.nop) + "\n")

        if cycle == 0:
            perm = "w"
        else:
            perm = "a"
        with open(self.opFilePath, perm) as wf:
            wf.writelines(printstate)


class FiveStageCore(Core):
    def __init__(self, io_dir, imem, dmem):
        super(FiveStageCore, self).__init__(io_dir + "/output/FS_", imem, dmem)
        self.opFilePath = io_dir + "/output/StateResult_FS.txt"

    def step(self):
        # Your implementation
        # --------------------- WB stage ---------------------

        # --------------------- MEM stage --------------------

        # --------------------- EX stage ---------------------

        # --------------------- ID stage ---------------------

        # --------------------- IF stage ---------------------

        self.halted = True
        if (
            self.state.IF.nop
            and self.state.ID.nop
            and self.state.EX.nop
            and self.state.MEM.nop
            and self.state.WB.nop
        ):
            self.halted = True

        self.myRF.output_RF(self.cycle)  # dump RF
        self.print_state(
            self.nextState, self.cycle
        )  # print states after executing cycle 0, cycle 1, cycle 2 ...

        self.state = (
            self.nextState
        )  # The end of the cycle and updates the current state with the values calculated in this cycle
        self.cycle += 1

    def print_state(self, state, cycle):
        printstate = [
            "-" * 70 + "\n",
            "State after executing cycle: " + str(cycle) + "\n",
        ]
        printstate.extend(
            ["IF." + key + ": " + str(val) + "\n" for key, val in state.IF.items()]
        )
        printstate.extend(
            ["ID." + key + ": " + str(val) + "\n" for key, val in state.ID.items()]
        )
        printstate.extend(
            ["EX." + key + ": " + str(val) + "\n" for key, val in state.EX.items()]
        )
        printstate.extend(
            ["MEM." + key + ": " + str(val) + "\n" for key, val in state.MEM.items()]
        )
        printstate.extend(
            ["WB." + key + ": " + str(val) + "\n" for key, val in state.WB.items()]
        )

        if cycle == 0:
            perm = "w"
        else:
            perm = "a"
        with open(self.opFilePath, perm) as wf:
            wf.writelines(printstate)


if __name__ == "__main__":

    # parse arguments for input file location
    parser = argparse.ArgumentParser(description="RV32I processor")
    parser.add_argument(
        "--io_dir",
        default="io_dir",
        type=str,
        help="Directory containing the input files.",
    )
    args = parser.parse_args()

    io_dir = os.path.abspath(args.io_dir)
    print("IO Directory:", io_dir)

    imem = InsMem("Imem", io_dir)
    dmem_ss = DataMem("SS", io_dir)
    dmem_fs = DataMem("FS", io_dir)

    ssCore = SingleStageCore(io_dir, imem, dmem_ss)
    # fsCore = FiveStageCore(io_dir, imem, dmem_fs)

    while True:
        if not ssCore.halted:
            ssCore.step()

        # if not fsCore.halted:
        #     fsCore.step()

        # if ssCore.halted and fsCore.halted:
        #     break

        if ssCore.halted:
            break

    # dump SS and FS data mem.
    dmem_ss.output_data_mem()
    dmem_fs.output_data_mem()
