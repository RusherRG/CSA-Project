from instruction import Instruction


class RType(Instruction):
    def __init__(self, rs1, rs2, rd):
        self.rs1 = rs1
        self.rs2 = rs2
        self.rd = rd
