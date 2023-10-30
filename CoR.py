from abc import abstractmethod


class IFactory:
    @abstractmethod
    def set_next_factory(self, factory: 'IFactory'):
        pass

    @abstractmethod
    def build(self, vehicle):
        pass


class ABCFactory(IFactory):
    def __init__(self):
        self._next_factory = None

    def set_next_factory(self, factory: IFactory):
        self._next_factory = factory
        return factory

    def build(self, vehicle):
        if self._next_factory is not None:
            return self._next_factory.build(vehicle)
        return ''


class BoatFactory(ABCFactory):
    def build(self, vehicle):
        if vehicle == 'boat':
            return "Factory build boat"
        else:
            return super().build(vehicle)


class CarFactory(ABCFactory):
    def build(self, vehicle):
        if vehicle == 'car':
            return "Factory build car"
        else:
            return super().build(vehicle)


class PlaneFactory(ABCFactory):
    def build(self, vehicle):
        if vehicle == 'plane':
            return "Factory build plane"
        else:
            return super().build(vehicle)


if __name__ == "__main__":
    car_factory = CarFactory()
    boat_factory = BoatFactory()
    plane_factory = PlaneFactory()

    car_factory.set_next_factory(boat_factory).set_next_factory(plane_factory)

    print(car_factory.build('car'))
    print(car_factory.build('plane'))

