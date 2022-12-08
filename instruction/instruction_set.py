from instruction import Instruction
from instruction.mnemonics import (
    Add,
    Sub,
    Xor,
    Or,
    And,
    Addi,
    Xori,
    Andi,
    Ori,
    Beq,
    Bne,
    LW,
    SW,
    Jal,
    HALT,
)


class InstructionSet:
    def decode(self, instr: str) -> Instruction:
        opcode = instr[:7][::-1]
        func3 = instr[12:15][::-1]
        if opcode == "0110011":
            func7 = "".join(instr[25:][::-1])
            if func3 == "000" and func7 == "0000000":
                # add instruction
                return Add()
            elif func3 == "000" and func7 == "0100000":
                # sub instruction
                return Sub()
            elif func3 == "100" and func7 == "0000000":
                # xor instruction
                return Xor()
            elif func3 == "110" and func7 == "0000000":
                # or instruction
                return Or()
            elif func3 == "111" and func7 == "0000000":
                # and instruction
                return And()
        elif opcode == "0010011":
            if func3 == "000":
                # addi instruction
                return Addi()
            elif func3 == "100":
                # xori instruction
                return Xori()
            elif func3 == "110":
                # ori instruction
                return Ori()
            elif func3 == "111":
                # andi instruction
                return Andi()
        elif opcode == "1101111":
            # jal instruction
            return Jal()
        elif opcode == "1100011":
            if func3 == "000":
                # beq instruction
                return Beq()
            elif func3 == "001":
                # bne instruction
                return Bne()
        elif opcode == "0000011":
            if func3 == "000":
                # lw instruction
                return LW()
        elif opcode == "0100011":
            if func3 == "010":
                # sw instruction
                return SW()
        # halt instruction
        return HALT()
