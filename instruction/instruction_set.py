from instruction import Instruction
from instruction.mnemonics import Add, Addi, LW, SW


class InstructionSet:
    def decode(self, instr: str) -> Instruction | None:
        opcode = instr[:7][::-1]
        func3 = instr[12:15][::-1]
        if opcode == "0110011":
            func7 = "".join(instr[25:][::-1])
            if func3 == "000" and func7 == "0000000":
                # add instruction
                return Add()
            elif func3 == "000" and func7 == "0100000":
                # sub instruction
                pass
            elif func3 == "100" and func7 == "0000000":
                # xor instruction
                pass
            elif func3 == "110" and func7 == "0000000":
                # or instruction
                pass
            elif func3 == "111" and func7 == "0000000":
                # and instruction
                pass
        elif opcode == "0010011":
            if func3 == "000":
                # addi instruction
                return Addi()
            elif func3 == "100":
                # xori instruction
                pass
            elif func3 == "110":
                # ori instruction
                pass
            elif func3 == "111":
                # andi instruction
                pass
        elif opcode == "1101111":
            # jal instruction
            pass
        elif opcode == "1100011":
            if func3 == "000":
                # beq instruction
                pass
            elif func3 == "001":
                # bne instruction
                pass
        elif opcode == "0000011":
            if func3 == "000":
                # lw instruction
                return LW()
        elif opcode == "0100011":
            if func3 == "010":
                # sw instruction
                return SW()
        elif opcode == "1111111":
            # halt instruction
            pass
        return None
