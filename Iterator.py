class CarFactory:
    def __iter__(self):
        self.__cars = 0
        return self

    def __next__(self):
        self.__cars += 1
        return self.__cars


if __name__ == "__main__":
    car_factory = CarFactory()
    car_builder = iter(car_factory)

    print("Count of built cars:" + str(next(car_builder)))
    print("Count of built cars:" + str(next(car_builder)))
    print("Count of built cars:" + str(next(car_builder)))
    print("Count of built cars:" + str(next(car_builder)))

