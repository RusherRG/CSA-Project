from utils import DataMem, RegisterFile, State
from instruction.states import (
    InstructionDecodeState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)


class Instruction:
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        pass

    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        pass

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        pass

    def writeback(self, wb_state: WriteBackState, rf: RegisterFile) -> None:
        if wb_state.write_enable:
            rf.write_RF(wb_state.write_reg_addr, wb_state.write_data)

    def run(self, state: State, rf: RegisterFile, data_mem: DataMem) -> None:
        self.decode(state.ID, state.EX, rf)
        self.execute(state.EX, state.MEM)
        self.memory_access(state.MEM, state.WB, data_mem)
        self.writeback(state.WB, rf)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"
