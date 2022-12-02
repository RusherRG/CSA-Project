from utils import RegisterFile, State


class InstructionDecodeStage:
    def __init__(
        self,
        state: State,
        rf: RegisterFile,
    ):
        self.state = state
        self.rf = rf

    def detect_hazard(self, rs):
        if rs == self.state.EX.write_reg_addr and self.state.MEM.read_mem == 0:
            # EX to 1st
            return 2
        elif rs == self.state.WB.write_reg_addr and self.state.WB.write_enable:
            # EX to 2nd
            # MEM to 2nd
            return 1
        elif rs == self.state.MEM.write_reg_addr and self.state.MEM.read_mem != 0:
            # MEM to 1st
            self.state.EX.nop = 1
            return 1
        else:
            return 0

    def read_data(self, rs, i):
        if self.state.EX.alu_op[i] == 1:
            return self.state.WB.write_data
        elif self.state.EX.alu_op[i] == 2:
            return self.state.MEM.alu_result
        else:
            return self.rf.read_RF(rs)

    def run(self):
        if self.state.ID.nop:
            self.state.ID.nop -= 1
            return

        self.state.EX.instr = self.state.ID.instr
        opcode = self.state.ID.instr[:7][::-1]
        
        if opcode == "0110011":
            # r-type instruction
            rs1 = int("0b" + self.state.ID.instr[15:20][::-1], 2)
            rs2 = int("0b" + self.state.ID.instr[20:25][::-1], 2)

            self.state.EX.alu_op[0] = self.detect_hazard(rs1)
            self.state.EX.alu_op[1] = self.detect_hazard(rs2)

            if self.state.EX.nop:
                return

            self.state.EX.read_data_1 = self.read_data(rs1, 0)
            self.state.EX.read_data_2 = self.read_data(rs2, 1)

            self.state.EX.write_reg_addr = int(
                "0b" + self.state.ID.instr[7:12][::-1], 2
            )
            self.state.EX.write_enable = 1

        elif opcode == "0010011" or opcode == "0000011":
            # i-type instruction
            rs1 = int("0b" + self.state.ID.instr[15:20][::-1], 2)

            self.state.EX.alu_op[0] = self.detect_hazard(rs1)
            if self.state.EX.nop:
                return

            self.state.EX.read_data_1 = self.read_data(rs1, 0)

            self.state.EX.write_reg_addr = int(
                "0b" + self.state.ID.instr[7:12][::-1], 2
            )
            self.state.EX.is_I_type = True
            if self.state.ID.instr[20:][::-1][0] == "0":
                self.state.EX.imm = int("0b" + self.state.ID.instr[20:-1][::-1], 2)
            else:
                self.state.EX.imm = -(
                    -int("0b" + self.state.ID.instr[20:-1][::-1], 2) & 0b11111111111
                )
            self.state.EX.write_enable = 1
        elif opcode == "1101111":
            # j-type instruction
            pass
        elif opcode == "1100011":
            # b-type instruction
            pass
        elif opcode == "0100011":
            # sw-type instruction
            rs1 = int("0b" + self.state.ID.instr[15:20][::-1], 2)
            rs2 = int("0b" + self.state.ID.instr[20:25][::-1], 2)

            self.state.EX.alu_op[0] = self.detect_hazard(rs1)
            self.state.EX.alu_op[1] = self.detect_hazard(rs2)

            if self.state.EX.nop:
                return

            self.state.EX.read_data_1 = self.read_data(rs1, 0)
            self.state.EX.read_data_2 = self.read_data(rs2, 1)

            self.state.EX.imm = int(
                "0b" + (self.state.ID.instr[7:12] + self.state.ID.instr[25:])[::-1], 2
            )
        else:
            # halt instruction
            self.state.ID.nop = 1
            return None
        return 1
