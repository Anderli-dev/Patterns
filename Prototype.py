from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __copy__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.other_properties = {}

    def __copy__(self):
        new = self.__class__()
        new.__dict__.update(self.__dict__)
        return new


if __name__ == "__main__":
    truck = Truck()

    print("Default:")
    print(truck.wheels)

    six_wheels_truck = truck.__copy__()
    six_wheels_truck.wheels += 2

    print("Six wheels:")
    print(six_wheels_truck.wheels)
