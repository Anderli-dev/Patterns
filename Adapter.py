from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, engine: str, hull: str):
        self.engine = engine
        self.hull = hull

    @abstractmethod
    def move(self):
        pass


class Plane(Vehicle):
    def __init__(self, engine="Plane engine", hull="Plane hull"):
        super().__init__(engine, hull)

    def move(self):
        print("Fly")


class Car(Vehicle):
    def __init__(self, engine="Car engine", hull="Car hull"):
        super().__init__(engine, hull)

    def move(self):
        print("Ride")


class Adapter:
    def adapt(self, cls: Vehicle, adapted: Vehicle):
        c = cls()
        adapted.hull = c.hull
        return adapted

if __name__ == "__main__":

    plane = Plane()
    print(plane.engine)
    print(plane.hull)

    adapter = Adapter()
    adapter.adapt(Car, plane)

    print("------------")
    print(plane.engine)
    print(plane.hull)
