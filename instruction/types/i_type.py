from instruction import Instruction
from instruction.states import ExecutionState, InstructionDecodeState
from utils import RegisterFile


class IType(Instruction):
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        ex_state.read_data_1 = rf.read_RF(int("0b" + id_state.instr[15:20][::-1], 2))
        ex_state.write_reg_addr = int("0b" + id_state.instr[7:12][::-1], 2)
        ex_state.is_I_type = True
        imm = id_state.instr[20:][::-1]
        if imm[0] == "0":
            ex_state.imm = int("0b" + imm[1:], 2)
        else:
            ex_state.imm = -(
                -int("0b" + imm[1:], 2) & 0b11111111111
            )
        ex_state.write_enable = 1
