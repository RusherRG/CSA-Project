from instruction.mnemonics import Add


class InstructionSet:
    def decode(self, instr):
        opcode = "".join(instr[:7][::-1])
        func3 = "".join(instr[12:15][::-1])
        if opcode == "0110011":
            func7 = "".join(instr[25:][::-1])
            if func3 == "000" and func7 == "0000000":
                # add instruction
                return Add(rs1=instr[15:20], rs2=instr[20:25], rd=instr[7:12])
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
                pass
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
                pass
        elif opcode == "0100011":
            if func3 == "010":
                # sw instruction
                pass
        elif opcode == "1111111":
            # halt instruction
            pass
        return None
