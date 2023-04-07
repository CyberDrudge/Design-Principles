class Computer:
    keyboard: Keyboard
    mouse: Mouse
    monitor: Monitor

    def __init__(self, keyboard, mouse, monitor):
        self.keyboard = keyboard
        self.mouse = mouse
        self.monitor = monitor


class Keyboard:
    pass


class WiredKeyboard(Keyboard):
    pass


class WirelessKeyboard(Keyboard):
    pass
