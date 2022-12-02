from utils import State

class ExecutionStage:
    def __init__(
        self,
        state: State
    ):
        self.state = state

    def run(self):
        if self.state.EX.nop:
            self.state.EX.nop -= 1
            return
        opcode = self.state.EX.instr[:7][::-1]
        func3 = self.state.EX.instr[12:15][::-1]

        self.state.EX.write_enable = 0
        self.state.MEM.read_mem = 0
        self.state.MEM.write_mem = 0
        if opcode == "0110011":
            self.state.EX.write_enable = 1
            func7 = "".join(self.state.EX.instr[25:][::-1])
            if func3 == "000" and func7 == "0000000":
                # add instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 + self.state.EX.read_data_2
                )
            elif func3 == "000" and func7 == "0100000":
                # sub instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 - self.state.EX.read_data_2
                )
            elif func3 == "100" and func7 == "0000000":
                # xor instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 ^ self.state.EX.read_data_2
                )
            elif func3 == "110" and func7 == "0000000":
                # or instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 | self.state.EX.read_data_2
                )
            elif func3 == "111" and func7 == "0000000":
                # and instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 & self.state.EX.read_data_2
                )
        elif opcode == "0010011":
            self.state.EX.write_enable = 1
            if func3 == "000":
                # addi instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 + self.state.EX.imm
                )
            elif func3 == "100":
                # xori instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 ^ self.state.EX.imm
                )
            elif func3 == "110":
                # ori instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 | self.state.EX.imm
                )
            elif func3 == "111":
                # andi instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 & self.state.EX.imm
                )
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
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 + self.state.EX.imm
                )
                self.state.MEM.read_mem = 1
                self.state.EX.write_enable = 1
        elif opcode == "0100011":
            if func3 == "010":
                # sw instruction
                self.state.MEM.alu_result = (
                    self.state.EX.read_data_1 + self.state.EX.imm
                )
                self.state.MEM.write_mem = 1
                self.state.MEM.store_data = self.state.EX.read_data_2
        self.state.MEM.write_enable = self.state.EX.write_enable
        self.state.MEM.write_reg_addr = self.state.EX.write_reg_addr
