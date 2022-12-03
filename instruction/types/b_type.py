from instruction import Instruction
from instruction.states import ExecutionState, InstructionDecodeState
from utils import RegisterFile


class BType(Instruction):
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        ex_state.read_data_1 = rf.read_RF(int("0b" + id_state.instr[15:20][::-1], 2))
        ex_state.read_data_2 = rf.read_RF(int("0b" + id_state.instr[20:25][::-1], 2))
        imm = (
            id_state.instr[8:12]
            + id_state.instr[25:31]
            + id_state.instr[7]
            + id_state.instr[31]
        )[::-1]
        if imm[0] == "0":
            ex_state.imm = int("0b" + imm, 2)
        else:
            ex_state.imm = -(
                -int(
                    "0b" + imm,
                    2,
                )
                & 0b11111111111
            )
        ex_state.imm = ex_state.imm << 1
