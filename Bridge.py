from abc import ABC, abstractmethod


class MoveMethod(ABC):
    @abstractmethod
    def move(self):
        pass


class Fly(MoveMethod):
    def move(self):
        print("Fly")


class Ride(MoveMethod):
    def move(self):
        print("Ride")


class Vehicle:
    def __init__(self, engine: str, hull: str, move_method: MoveMethod):
        self.engine = engine
        self.hull = hull
        self.move_method = move_method

    def move(self):
        self.move_method.move()


class Plane(Vehicle):
    def __init__(self, move_method, engine="Plane engine", hull="Plane hull"):
        super().__init__(engine, hull, move_method)


class Car(Vehicle):
    def __init__(self, move_method, engine="Car engine", hull="Car hull"):
        super().__init__(engine, hull, move_method)


if __name__ == "__main__":

    car = Car(Ride())
    plane = Plane(Fly())

    car.move()

    plane.move()

    plane = Plane(Ride())
    print("Now plane ride")
    plane.move()
