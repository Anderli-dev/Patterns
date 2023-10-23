class Truck:
    def __init__(self):
        self.wheels = 0
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Truck, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == "__main__":
    truck = Truck()
    truck2 = Truck()

    print(truck.wheels)
    print(truck2.wheels)

    truck.wheels = 4

    print(truck.wheels)
    print(truck2.wheels)
