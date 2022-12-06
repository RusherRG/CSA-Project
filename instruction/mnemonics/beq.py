from instruction.states import (
    InstructionFetchState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from instruction.types import BType
from utils import DataMem, RegisterFile, bin2int, int2bin


class Beq(BType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.alu_result = int2bin(
            bin2int(ex_state.read_data_1, sign_ext=True)
            - bin2int(ex_state.read_data_2, sign_ext=True)
        )
        mem_state.store_data = ex_state.imm

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        if mem_state.alu_result == "0" * 32:
            wb_state.write_data = mem_state.store_data
            wb_state.write_enable = True
        else:
            wb_state.write_enable = False

    def writeback(
        self,
        wb_state: WriteBackState,
        if_state: InstructionFetchState,
        rf: RegisterFile,
    ) -> None:
        if wb_state.write_enable:
            if_state.PC += bin2int(wb_state.write_data, sign_ext=True)
        else:
            if_state.PC += 4
