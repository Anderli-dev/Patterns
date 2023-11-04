from typing import List


class Memento:
    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Car:
    def __init__(self):
        self.__state: List[str] = ['hull']

    def add_component(self, ingredient: str) -> None:
        self.__state.append(ingredient)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Car components: {self.__state}"


class Factory:
    def __init__(self, car: Car):
        self.car = car
        self.car_states: List[Memento] = []

    def add_component_to_car(self, component: str):
        self.car_states.append(self.car.create_memento())
        self.car.add_component(component)

    def undo_add_component(self):
        if len(self.car_states) == 1:
            self.car.set_memento(self.car_states[0])
            print(self.car)
        else:
            state = self.car_states.pop()
            self.car.set_memento(state)
            print(self.car)


if __name__ == "__main__":
    car = Car()
    factory = Factory(car)

    print(car)

    factory.add_component_to_car("wheel")
    factory.add_component_to_car("wheel")
    factory.add_component_to_car("wheel")
    factory.add_component_to_car("wheel")
    print(car)

    factory.add_component_to_car("wheel")
    factory.add_component_to_car("wheel")
    print(car)

    factory.undo_add_component()
    factory.undo_add_component()
    print(car)
