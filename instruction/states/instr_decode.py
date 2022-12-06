class InstructionDecodeState:
    def __init__(self) -> None:
        self.nop: int = 1
        self.instr: str = "0"*32

    def __dict__(self):
        return {"nop": self.nop, "Instr": self.instr}
