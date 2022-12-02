from utils import InsMem, State


class InstructionFetchStage:
    def __init__(
        self,
        state: State,
        ins_mem: InsMem,
    ):
        self.state = state
        self.ins_mem = ins_mem

    def run(self):
        if self.state.IF.nop:
            self.state.IF.nop -= 1
            return
        self.state.ID.instr = self.ins_mem.read_instr(self.state.IF.PC)[::-1]
        self.state.IF.PC += 4
