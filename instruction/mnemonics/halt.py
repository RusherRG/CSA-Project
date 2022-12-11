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
        id_state.nop = True

    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        ex_state.nop = True

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        mem_state.nop = True

    def writeback(self, wb_state: WriteBackState, if_state: InstructionFetchState, rf: RegisterFile) -> None:
        wb_state.nop = True
        if_state.nop = True
