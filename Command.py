from abc import abstractmethod
from typing import List, Deque


class IFactory:
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def build(self):
        pass


class CarFactory(IFactory):
    def on(self):
        print("Build car begin")

    def off(self):
        print("Build car stop")

    def build(self):
        print("Build car")


class BoatFactory(IFactory):
    def on(self):
        print("Build boat begin")

    def off(self):
        print("Build boat stop")

    def build(self):
        print("Build boat")


class CommandConsole:
    def __init__(self):
        self.__commands: List[IFactory] = [None, None]
        self.__history: Deque[IFactory] = []

    def set_command(self, button, command: IFactory):
        self.__commands[button] = command

    def pres_on(self, button):
        self.__commands[button].on()
        self.__history.append(self.__commands[button])

    def build(self):
        if len(self.__history) != 0:
            self.__history[-1].build()
        else:
            print('All factory stopped')

    def pres_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().off()


if __name__ == '__main__':
    car_factory = CarFactory()
    boat_factory = BoatFactory()

    console = CommandConsole()

    console.set_command(0, car_factory)
    console.set_command(1, boat_factory)

    console.pres_on(0)
    console.pres_on(1)

    # Build boat
    console.build()

    # Build car
    console.pres_cancel()
    console.build()

    # Build boat
    console.pres_on(1)
    console.build()

    # stop all
    console.pres_cancel()
    console.pres_cancel()

    # can`t build
    console.build()



