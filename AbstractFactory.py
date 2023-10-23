from abc import ABC, abstractmethod


class Fabric(ABC):
    @abstractmethod
    def create_ship(self):
        pass

    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_plane(self):
        pass


class Vehicle:
    def __init__(self, engine: str, hull: str):
        self.engine = engine
        self.hull = hull

    @abstractmethod
    def get_vehicle(self):
        print(self.engine)
        print(self.hull)

    @abstractmethod
    def move(self):
        pass


class Ship(Vehicle):
    def __init__(self, engine="Ship engine", hull="Ship hull"):
        super().__init__(engine, hull)

    def move(self):
        print("Swim")


class Car(Vehicle):
    def __init__(self, engine="Car engine", hull="Car hull"):
        super().__init__(engine, hull)

    def move(self):
        print("Ride")

class Plane(Vehicle):
    def __init__(self, engine="Plane engine", hull="Plane hull"):
        super().__init__(engine, hull)

    def move(self):
        print("Fly")


class Boat(Ship):
    pass


class Submarine(Ship):
    pass


class Truck(Car):
    def whoI(self):
        print("Im truck")


class ArmoredCar(Car):
    def whoI(self):
        print("Im fighting vehicle")


class TransportPlane(Plane):
    pass


class FighterJet(Plane):
    pass


class CommercialFabric(Fabric):
    def create_car(self):
        return ArmoredCar()

    def create_plane(self):
        return FighterJet()

    def create_ship(self):
        return Submarine()


class MilitaryFabric(Fabric):
    def create_car(self):
        return Truck()

    def create_plane(self):
        return TransportPlane()

    def create_ship(self):
        return Boat()


if __name__ == "__main__":
    commercial_fabric = CommercialFabric()
    military_fabric = MilitaryFabric()

    print("It`s")
    car = commercial_fabric.create_car()
    car.whoI()

    print("It`s")
    car = military_fabric.create_car()
    car.whoI()
