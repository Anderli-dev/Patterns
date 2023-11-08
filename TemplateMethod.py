from abc import abstractmethod


class Factory:
    def build(self):
        self.car_build()
        self.boat_build()

    @abstractmethod
    def car_build(self):
        pass

    @abstractmethod
    def boat_build(self):
        pass


class Factory1(Factory):
    def car_build(self):
        print("Build car")

    def boat_build(self):
        print("Build boat")


class Factory2(Factory):
    def car_build(self):
        print("Build car with 6 wheels")

    def boat_build(self):
        print("Build yacht")


def factory_build(factory: Factory):
    factory.build()


if __name__ == "__main__":
    factory_build(Factory1())
    factory_build(Factory2())
