class ParkingLot:
    def park_car(self):
        # Decrease empty slots by 1
        raise NotImplementedError

    def unpark_car(self):
        # Increase empty slots by 1
        raise NotImplementedError

    def get_capacity(self):
        # Returns empty slots' count
        raise NotImplementedError

    def calculate_fee(self, car):
        # Returns the parking fee
        raise NotImplementedError

    def take_payment(self, car):
        # Take Payment
        raise NotImplementedError


class FreeParkingLot:
    def park_car(self):
        pass

    def unpark_car(self):
        pass

    def get_capacity(self):
        pass

    def calculate_fee(self, car):
        raise Exception("There is no fee. This parking is free.")

    def take_payment(self, car):
        raise Exception("Cannot take payment. This parking is free.")
