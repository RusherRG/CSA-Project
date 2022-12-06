class InstructionFetchState:
    def __init__(self) -> None:
        self.nop: int = 0
        self.PC: int = 0

    def __dict__(self):
        return {"nop": self.nop, "PC": self.PC}
