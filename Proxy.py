from abc import abstractmethod, ABCMeta


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def get_car(self, num):
        pass


class Car(ICar):
    def get_car(self, brand):
        return 'This is car {}'.format(brand)


class CarRent(ICar):
    def __init__(self, car):
        self._car = car
        self._storage = {}

    def get_car(self, brand):
        car = ''

        if self._storage.get(brand) is not None:
            # get car from storage
            car = self._storage[brand]
            car = 'from storage: ' + car
        else:
            # get(buy) new car for rental
            car = self._car.get_car(brand)
            self._storage[brand] = car
        return car


if __name__ == "__main__":
    car_rent = CarRent(Car())

    # order of rent
    print(car_rent.get_car("BMW"))
    print(car_rent.get_car("FORD"))
    print(car_rent.get_car("LANOS"))

    print(car_rent.get_car("FORD"))
