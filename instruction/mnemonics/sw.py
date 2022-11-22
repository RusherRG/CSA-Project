from instruction.states import (
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import BType
from utils import DataMem


class SW(BType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.write_mem = ex_state.imm + ex_state.read_data_1
        mem_state.store_data = ex_state.read_data_2

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        data_mem.write_data_mem(mem_state.write_mem, mem_state.store_data)
