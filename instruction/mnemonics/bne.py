from instruction.states import (
    InstructionFetchState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import BType
from utils import DataMem, RegisterFile


class Bne(BType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.alu_result = int(ex_state.read_data_1 != ex_state.read_data_2)
        mem_state.store_data = ex_state.imm

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        if mem_state.alu_result:
            wb_state.write_data = mem_state.store_data
            wb_state.write_enable = 1
        else:
            wb_state.write_enable = 0

    def writeback(
        self,
        wb_state: WriteBackState,
        if_state: InstructionFetchState,
        rf: RegisterFile,
    ) -> None:
        if wb_state.write_enable:
            if_state.PC += wb_state.write_data
        else:
            if_state.PC += 4
