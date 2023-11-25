"""
@Author: Jesus Ramos Membrive
@Date: 25/11/2023
@Link: ramos.membrive@gmail.com
@Description:
    Inheritance allows us to create a new class from an existing class.

    The new class that is created is known as subclass (child or derived class) and the existing class from which the child
    class is derived is known as superclass (parent or base class).
"""


class Vehicle:
    """
    This is the superclass.
    """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return "The engine has started."

    @staticmethod
    def stop_engine():
        return "The engine has stopped."


class Car(Vehicle):  # Inherits from Vehicle.
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    @staticmethod
    def play_radio():
        return "The radio is playing."


class Truck(Vehicle):  # Inherits from Vehicle.
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def unload_cargo(self):
        return f"Unloading {self.load_capacity} kg of load."


class ElectricVehicle:
    @staticmethod
    def charge_battery():
        return "Battery charging."


class ElectricCar(Car, ElectricVehicle):  # Multiple inheritance.
    def __init__(self, brand, model, seats, battery_range):
        Car.__init__(self, brand, model, seats)
        self.battery_range = battery_range

    def start_engine(self):
        return "Electric motor started silently."


# Creating objects of different classes.
my_car = Car("Toyota", "Corolla", 5)
my_truck = Truck("Volvo", "VNL", 20000)
my_electric_car = ElectricCar("Tesla", "Model S", 5, 400)

# Usage examples
print(my_car.start_engine())
print(my_truck.unload_cargo())
print(my_electric_car.charge_battery())
print(my_electric_car.start_engine())
