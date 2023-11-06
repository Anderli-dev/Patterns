from abc import abstractmethod


class Factory:
    _vehicle = None

    def __init__(self, vehicle):
        self.transition_to(vehicle)

    def transition_to(self, vehicle):
        self._vehicle = vehicle
        self._vehicle.context = self

    def product_ride(self):
        self._vehicle.ride()


class Vehicle:
    @property
    def context(self):
        return self._factory

    @context.setter
    def context(self, factory):
        self._factory = factory

    @abstractmethod
    def ride(self):
        pass


class Car(Vehicle):
    def ride(self):
        print("Car ride")
        self._factory.transition_to(Truck())


class Truck(Vehicle):
    def ride(self):
        print("Truck ride")
        self._factory.transition_to(Car())


if __name__ == "__main__":
    factory = Factory(Car())

    factory.product_ride()
    factory.product_ride()
