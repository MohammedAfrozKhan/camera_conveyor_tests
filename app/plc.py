class FakePLC:
    """
    Fake PLC class simulating start/stop cycle and module out.
    """
    def __init__(self):
        self.started = False
        self.module_out = False

    def start_cycle(self):
        self.started = True

    def set_module_out(self):
        self.module_out = True

    def stop(self):
        self.started = False
