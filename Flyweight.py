class CarFlyWeight:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


class Car:
    def __init__(self, owner, flyweight: CarFlyWeight):
        self.owner = owner
        self.flyweight = flyweight


class CarFactory:
    def __init__(self):
        self.car_list = []

    def get_flyweight(self, color, brand):
        flyweights = list(filter(lambda x: x.color == color and x.brand == brand, self.car_list))
        if flyweights:
            return flyweights[0]
        else:
            flyweight = CarFlyWeight(color, brand)
            self.car_list.append(flyweight)
            return flyweight


if __name__ == "__main__":
    cars = []

    car_factory = CarFactory()

    flyweight = car_factory.get_flyweight("red", "BMW")
    car = Car(1, flyweight)
    cars.append(car)

    flyweight = car_factory.get_flyweight("red", "BMW")
    car = Car(2, flyweight)
    cars.append(car)

    flyweight = car_factory.get_flyweight("blue", "BMW")
    car = Car(3, flyweight)
    cars.append(car)

    for car in cars:
        print("Owner id " + str(car.owner))
        print("Memory cell", car.flyweight)
