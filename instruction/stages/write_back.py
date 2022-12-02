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
            self.state.WB.nop -= 1
            return
        if self.state.WB.write_enable and self.state.WB.write_data:
            self.rf.write_RF(self.state.WB.write_reg_addr, self.state.WB.write_data)
