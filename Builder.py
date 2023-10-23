from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class FabricBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_wheels(self) -> None:
        pass

    @abstractmethod
    def add_armor(self) -> None:
        pass


class TruckBuilder(FabricBuilder):
    def __init__(self):
        self._truck = Truck()

    def _clear(self):
        self._truck = Truck()

    @property
    def product(self) -> Truck:
        truck = self._truck
        self._clear()
        return truck

    def add_wheels(self):
        self._truck.wheels += 2

    def add_armor(self):
        _dict = self._truck.__dict__["armor"] = 100


class Truck:
    def __init__(self):
        self.wheels = 4
        self.other_properties = {}


if __name__ == "__main__":
    builder = TruckBuilder()
    default_truck = builder.product
    print(default_truck.__dict__)

    builder.add_wheels()
    six_wheels_truck = builder.product
    print(six_wheels_truck.__dict__)

    builder.add_wheels()
    builder.add_armor()
    armored_truck = builder.product
    print(armored_truck.__dict__)


