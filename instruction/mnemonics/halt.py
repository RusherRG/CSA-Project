from instruction import Instruction
from instruction.states import (
    InstructionFetchState,
    InstructionDecodeState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from utils import DataMem, RegisterFile


class HALT(Instruction):
    def decode(
        self,
        id_state: InstructionDecodeState,
        ex_state: ExecutionState,
        rf: RegisterFile,
    ) -> None:
        id_state.nop = 1

    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        ex_state.nop = 1

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        mem_state.nop = 1

    def writeback(self, wb_state: WriteBackState, if_state: InstructionFetchState, rf: RegisterFile) -> None:
        wb_state.nop = 1
        if_state.nop = 1
