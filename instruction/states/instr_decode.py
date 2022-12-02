class InstructionDecodeState:
    def __init__(self) -> None:
        self.nop = 1
        self.instr: str = ""

    def __dict__(self):
        return {"nop": self.nop, "Instr": self.instr}
