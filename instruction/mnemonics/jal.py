from instruction.types import JType
from instruction.states import (
    InstructionFetchState,
    ExecutionState,
    MemoryAccessState,
    WriteBackState,
)
from utils import DataMem, RegisterFile, bin2int, int2bin


class Jal(JType):
    def execute(self, ex_state: ExecutionState, mem_state: MemoryAccessState) -> None:
        mem_state.write_enable = ex_state.write_enable
        mem_state.write_reg_addr = ex_state.write_reg_addr
        mem_state.store_data = ex_state.imm

    def memory_access(
        self, mem_state: MemoryAccessState, wb_state: WriteBackState, data_mem: DataMem
    ) -> None:
        wb_state.write_enable = mem_state.write_enable
        wb_state.write_reg_addr = mem_state.write_reg_addr
        wb_state.write_data = mem_state.store_data

    def writeback(
        self,
        wb_state: WriteBackState,
        if_state: InstructionFetchState,
        rf: RegisterFile,
    ) -> None:
        if wb_state.write_enable:
            rf.write_RF(wb_state.write_reg_addr, int2bin(if_state.PC + 4))
            if_state.PC += bin2int(wb_state.write_data, sign_ext=True)
