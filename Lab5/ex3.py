class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, liters_per_100km):
        super().__init__(make, model, year)
        self.liters_per_100km = liters_per_100km

    def calculate_mileage(self, liters):
        return 100 * liters / self.liters_per_100km


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, liters_per_100km):
        super().__init__(make, model, year)
        self.liters_per_100km = liters_per_100km

    def calculate_mileage(self, liters):
        return 100 * liters / self.liters_per_100km


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return f"Towing Capacity: {self.towing_capacity} kg"


if __name__ == '__main__':
    ford = Car("Ford", "Fiesta", 2019, 7)
    print(ford.get_vehicle_info())
    print(ford.calculate_mileage(30))

    print()
    motorcycle = Motorcycle("Honda", "CBR", 2019, 3)
    print(motorcycle.get_vehicle_info())
    print(motorcycle.calculate_mileage(10))

    print()
    truck = Truck("Ford", "F-150", 2019, 200)
    print(truck.get_vehicle_info())
    print(truck.get_towing_capacity())

