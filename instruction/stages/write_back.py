from utils import RegisterFile, State


class WriteBackStage:
    def __init__(
        self,
        state: State,
        rf: RegisterFile,
    ):
        self.state = state
        self.rf = rf

    def run(self):
        if self.state.WB.nop:
            if not self.state.MEM.nop:
                self.state.WB.nop = False
            return
        if self.state.WB.write_enable:
            self.rf.write_RF(self.state.WB.write_reg_addr, self.state.WB.write_data)

        if self.state.MEM.nop:
            self.state.WB.nop = True
