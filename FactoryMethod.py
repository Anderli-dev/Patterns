from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class TruckCreator(Creator):
    def create_vehicle(self) -> Vehicle:
        return Vehicle("Gas engine", "Truck hull")


class BoatCreator(Creator):
    def create_vehicle(self) -> Vehicle:
        return Vehicle("Gas engine", "Boat hull")


class Vehicle:
    def __init__(self, engine: str, hull: str):
        self.engine = engine
        self.hull = hull

    @abstractmethod
    def get_vehicle(self):
        print(self.engine)
        print(self.hull)


if __name__ == "__main__":
    truck = TruckCreator().create_vehicle()
    boat = BoatCreator().create_vehicle()

    print("Boat:")
    print(boat.get_vehicle())

    print("Truck:")
    print(truck.get_vehicle())
