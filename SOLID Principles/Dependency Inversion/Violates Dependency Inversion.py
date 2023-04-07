class Computer:
    keyboard: WiredKeyboard
    mouse: WiredMouse
    monitor: Monitor

    def __init__(self):
        self.keyboard = WiredKeyboard()
        self.mouse = WiredMouse()
        self.monitor = Monitor()
