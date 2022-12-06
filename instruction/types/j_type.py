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
        ex_state.write_reg_addr = id_state.instr[7:12][::-1]
        ex_state.imm = (
            "0"
            + id_state.instr[21:31]
            + id_state.instr[20]
            + id_state.instr[12:20]
            + id_state.instr[31]
        )[::-1]
        ex_state.write_enable = True
