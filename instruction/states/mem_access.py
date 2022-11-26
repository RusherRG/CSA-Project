class MemoryAccessState:
    def __init__(self) -> None:
        self.nop = False
        self.alu_result = 0
        self.store_data = 0
        self.rs = 0
        self.rt = 0
        self.write_reg_addr = 0
        self.read_mem = 0
        self.write_mem = 0
        self.write_enable = 0

    def __dict__(self):
        return {
            "nop": self.nop,
            "ALUresult": self.alu_result,
            "Store_data": self.store_data,
            "Rs": self.rs,
            "Rt": self.rt,
            "Wrt_reg_addr": self.write_reg_addr,
            "rd_mem": self.read_mem,
            "wrt_mem": self.write_mem,
            "wrt_enable": self.write_enable,
        }
