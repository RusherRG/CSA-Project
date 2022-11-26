from instruction.states import (
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import IType
from utils import DataMem


class LW(IType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.read_mem = ex_state.imm + ex_state.read_data_1
        mem_state.write_enable = ex_state.write_enable
        mem_state.write_reg_addr = ex_state.write_reg_addr

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        mem_data_bin = "0b" + "".join(data_mem.read_data_mem(mem_state.read_mem))
        wb_state.write_data = int(mem_data_bin, 2)
        wb_state.write_enable = mem_state.write_enable
        wb_state.write_reg_addr = mem_state.write_reg_addr
