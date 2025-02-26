class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type

    def describe(self):
        return f"Bike Make: {self.make}, Model: {self.model}, Type: {self.bike_type}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors, price):
        super().__init__(make, model)
        self.num_doors = num_doors
        self.__price = price

    def get_price(self):
        return f"Car price: ${self.__price}"

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")


vehicles = [
    Car("Mustang", "Ford", 4, 150000),
    Bike("McLaren", "MC", "Sport"),
    Vehicle("Ford", "Transit")
]

for v in vehicles:
    print(v.describe())
