

class Car:
    def __init__(self, observer):
        self.wheels = 4
        self._observer = observer

    def notify(self) -> None:
        observer.update(self)

    def add_wheel(self):
        self.wheels += 1
        self.notify()


class Observer:

    def update(self, car: Car):
        if car.wheels >= 6:
            print("It`s truck")


if __name__ == "__main__":
    observer = Observer()
    car = Car(observer)

    print(car.wheels)

    car.add_wheel()
    car.add_wheel()
    print(car.wheels)

