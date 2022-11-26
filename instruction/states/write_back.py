class WriteBackState:
    def __init__(self) -> None:
        self.nop = False
        self.write_data = 0
        self.rs = 0
        self.rt = 0
        self.write_reg_addr = 0
        self.write_enable = 0

    def __dict__(self):
        return {
            "nop": self.nop,
            "Wrt_data": self.write_data,
            "Rs": self.rs,
            "Rt": self.rt,
            "Wrt_reg_addr": self.write_reg_addr,
            "wrt_enable": self.write_enable,
        }
