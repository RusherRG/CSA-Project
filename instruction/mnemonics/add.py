from instruction.states import (
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import RType
from utils import DataMem


class Add(RType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.alu_result = ex_state.read_data_1 + ex_state.read_data_2
        mem_state.write_enable = ex_state.write_enable
        mem_state.write_reg_addr = ex_state.write_reg_addr

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        wb_state.write_data = mem_state.alu_result
        wb_state.write_enable = mem_state.write_enable
        wb_state.write_reg_addr = mem_state.write_reg_addr
