from utils import DataMem, State


class MemoryAccessStage:
    def __init__(
        self, state: State, data_mem: DataMem
    ):
        self.state = state
        self.data_mem = data_mem

    def run(self):
        if self.state.MEM.nop:
            if not self.state.EX.nop:
                self.state.MEM.nop = False
            return
        if self.state.MEM.read_mem != 0:
            self.state.WB.write_data = self.data_mem.read_data_mem(self.state.MEM.alu_result)
        elif self.state.MEM.write_mem != 0:
            self.data_mem.write_data_mem(
                self.state.MEM.alu_result, self.state.MEM.store_data
            )
        else:
            self.state.WB.write_data = self.state.MEM.alu_result
            self.state.MEM.store_data = self.state.MEM.alu_result
        self.state.WB.write_enable = self.state.MEM.write_enable
        self.state.WB.write_reg_addr = self.state.MEM.write_reg_addr

        if self.state.EX.nop:
            self.state.MEM.nop = True
