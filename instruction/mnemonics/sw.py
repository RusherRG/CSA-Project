from instruction.states import (
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import SType
from utils import DataMem, bin2int, int2bin


class SW(SType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.write_mem = True
        mem_state.alu_result = int2bin(
            bin2int(ex_state.imm, sign_ext=True)
            + bin2int(ex_state.read_data_1, sign_ext=True)
        )
        mem_state.store_data = ex_state.read_data_2

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        if mem_state.write_mem == True:
            data_mem.write_data_mem(mem_state.alu_result, mem_state.store_data)
