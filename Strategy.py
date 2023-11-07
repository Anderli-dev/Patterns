from abc import abstractmethod


class Car:
    pass


class Factory:
    @abstractmethod
    def build(self):
        pass


class CarFactory(Factory):
    def build(self):
        print("Build car")


class BoatFactory(Factory):
    def build(self):
        print("Build boat")


class FlexFactory:
    def __init__(self, factory: Factory):
        self.base_factory = factory

    def build(self):
        self.base_factory.build()


if __name__ == "__main__":
    flex_factory = FlexFactory(CarFactory())

    flex_factory.build()

    flex_factory.base_factory = BoatFactory()

    flex_factory.build()
