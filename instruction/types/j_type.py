from instruction import Instruction
from instruction.states import InstructionDecodeState, ExecutionState
from utils import RegisterFile


class JType(Instruction):
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        ex_state.write_reg_addr = int("0b" + id_state.instr[7:12][::-1], 2)
        imm = (
            id_state.instr[21:31]
            + id_state.instr[20]
            + id_state.instr[12:20]
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
        ex_state.write_enable = 1
