
class Bike:
    def __init__(self):
        self.engine_status = "OFF"
        self.speed = 0

    def start_engine(self):
        self.engine_status = "ON"

    def accelerate(self):
        self.speed += 5

    def honk(self):
        print("Beep Boop")


class Bicycle(Bike):
    def start_engine(self):
        raise Exception("Cannot start engine. Engine Does not Exist")

    def accelerate(self):
        self.speed += 1

    def honk(self):
        print("Ting Ting")
