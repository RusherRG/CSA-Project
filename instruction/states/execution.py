class ExecutionState:
    def __init__(self) -> None:
        self.nop = False
        self.read_data_1 = 0
        self.read_data_2 = 0
        self.imm = 0
        self.rs = 0
        self.rt = 0
        self.write_reg_addr = 0
        self.is_I_type = False
        self.read_mem = 0
        self.write_mem = 0
        self.alu_op = 0
        self.write_enable = 0

    def __dict__(self):
        return {
            "nop": self.nop,
            "Read_data1": self.read_data_1,
            "Read_data2": self.read_data_2,
            "Imm": self.imm,
            "Rs": self.rs,
            "Rt": self.rt,
            "Wrt_reg_addr": self.write_reg_addr,
            "is_I_type": self.is_I_type,
            "rd_mem": self.read_mem,
            "wrt_mem": self.write_mem,
            "alu_op": self.alu_op,
            "wrt_enable": self.write_enable,
        }
