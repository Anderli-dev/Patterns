class Vehicle:
    def __init__(self, move_type: str):
        self.move_type = move_type

    def move(self):
        print(self.move_type)


class Truck(Vehicle):
    pass


class Car(Vehicle):
    pass


class Boat(Vehicle):
    pass


class MovingVehicles:
    def __init__(self, truck: Truck, car: Car, boat: Boat):
        self.truck = truck
        self.car = car
        self.boat = boat

    def move(self):
        self.truck.move()
        self.car.move()
        self.boat.move()


if __name__ == "__main__":
    car = Car("Car move")
    truck = Truck("Truck move")
    boat = Boat("Boat move")

    vehicles = MovingVehicles(truck, car, boat)
    vehicles.move()
