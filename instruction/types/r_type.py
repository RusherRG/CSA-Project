from instruction import Instruction
from instruction.states import ExecutionState, InstructionDecodeState
from utils import RegisterFile


class RType(Instruction):
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        ex_state.rs = id_state.instr[15:20][::-1]
        ex_state.rt = id_state.instr[20:25][::-1]
        ex_state.read_data_1 = rf.read_RF(ex_state.rs)
        ex_state.read_data_2 = rf.read_RF(ex_state.rt)
        ex_state.write_reg_addr = id_state.instr[7:12][::-1]
        ex_state.write_enable = True
