class InstructionFetchState:
    def __init__(self) -> None:
        self.nop = False
        self.PC: int = 0

    def items(self):
        return {"nop": self.nop, "PC": self.PC}
