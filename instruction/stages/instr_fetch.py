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
        if self.state.IF.nop or (self.state.EX.nop and not self.state.MEM.nop):
            return
        instr = self.ins_mem.read_instr(self.state.IF.PC)[::-1]
        if instr == "1" * 32:
            self.state.IF.nop = True
        else:
            if not self.state.ID.nop:
                self.state.IF.PC += 4
                self.state.ID.instr = instr
