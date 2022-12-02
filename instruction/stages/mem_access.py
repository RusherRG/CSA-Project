from utils import DataMem, State


class MemoryAccessStage:
    def __init__(
        self, state: State, data_mem: DataMem
    ):
        self.state = state
        self.data_mem = data_mem

    def run(self):
        if self.state.MEM.nop:
            self.state.MEM.nop -= 1
            return
        if self.state.MEM.read_mem != 0:
            mem_data_bin = "0b" + "".join(
                self.data_mem.read_data_mem(self.state.MEM.alu_result)
            )
            self.state.WB.write_data = int(mem_data_bin, 2)
        elif self.state.MEM.write_mem != 0:
            self.data_mem.write_data_mem(
                self.state.MEM.alu_result, self.state.MEM.store_data
            )
        else:
            self.state.WB.write_data = self.state.MEM.alu_result
            self.state.MEM.store_data = self.state.MEM.alu_result
        self.state.WB.write_enable = self.state.MEM.write_enable
        self.state.WB.write_reg_addr = self.state.MEM.write_reg_addr