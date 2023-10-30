from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self, price):
        self.price = price
        self.items: [Object] = []

    def get_price(self):
        if self.items is not []:
            price = self.price
            for i in self.items:
                price += i.get_price()
            return price
        else:
            return self.price


class Door(Object):
    pass


class Wheel(Object):
    pass


class Car(Object):
    def __init__(self, price, *items):
        super().__init__(price)
        self.items = [*items]


if __name__ == "__main__":
    door = Door(20)
    door1 = Door(20)

    wheel = Wheel(10)
    wheel1 = Wheel(10)
    wheel2 = Wheel(10)
    wheel3 = Wheel(10)

    car = Car(100, door, door1, wheel, wheel1, wheel2, wheel3)

    print(car.get_price())
