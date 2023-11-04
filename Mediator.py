class Factory:
    def __init__(self) -> None:
        self.mediator = None


class CarFactory(Factory):
    def build_car(self):
        print("Factory build")
        print("Build car")
        self.mediator.build(self, 0)


class BoatFactory(Factory):
    def build_boat(self):
        print("Factory build")
        print("Build boat")
        self.mediator.build(self, 1)


class PlaneFactory(Factory):
    def build_plane(self):
        print("Factory build")
        print("Build plane")
        self.mediator.build(self, 2)


class Mediator:
    def __init__(self, car_factory: CarFactory, boat_factory: BoatFactory, plane_factory: PlaneFactory):
        self.car_factory = car_factory
        self.car_factory.mediator = self
        self.boat_factory = boat_factory
        self.boat_factory.mediator = self
        self.plane_factory = plane_factory
        self.plane_factory.mediator = self

    def build(self, sender: object, build_type):
        if build_type == 0:
            # Разом з машиною будуються і інші транспортні засоби
            # Тобто взаємодія відбувається зерез посередника а не напряму
            print("Mediator build")
            self.plane_factory.build_plane()
            print("\n", end="")
        if build_type == 2:
            print("Mediator build")
            self.boat_factory.build_boat()
            print("\n", end="")


if __name__ == "__main__":
    car_factory = CarFactory()
    boat_factory = BoatFactory()
    plane_factory = PlaneFactory()

    mediator = Mediator(car_factory, boat_factory, plane_factory)

    car_factory.build_car()

    boat_factory.build_boat()


