# use default python decorator instead

class Vehicle:
    def __init__(self, move_type: str):
        self.move_type = move_type

    def move(self):
        print(self.move_type)


class GroundVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    def __init__(self, move_type: str, vehicle: Vehicle):
        super().__init__(move_type + vehicle.move_type)


if __name__ == "__main__":
    car = GroundVehicle("Ride")
    swimming_car = WaterVehicle("Swim ", car)

    swimming_car.move()
