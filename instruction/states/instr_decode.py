class InstructionDecodeState:
    def __init__(self) -> None:
        self.nop = False
        self.instr: str = ""

    def items(self):
        return {"nop": self.nop, "Instr": self.instr}
