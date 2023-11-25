"""
@Author: Jesus Ramos Membrive
@Date: 25/11/2023
@Link: ramos.membrive@gmail.com
@Description:
    Encapsulation is a fundamental concept in object-oriented programming (OOP) that refers to restricting access to
    methods and variables to prevent unintentional modification of data.
"""


class Car:
    def __init__(self, color):
        self._speed = 0  # Private attribute.
        self._color = color  # Private attribute

    def accelerate(self, increment):
        """ Increments the speed of the car. """
        self._speed += increment

    def brake(self, decrement):
        """ Decrements the speed of the car. """
        if self._speed - decrement >= 0:
            self._speed -= decrement
        else:
            self._speed = 0

    def get_speed(self):
        """ Returns the current speed of the car. """
        return self._speed

    def set_color(self, color):
        """ Sets the color of the car. """
        self._color = color

    def get_color(self):
        """ Returns the current color of the car. """
        return self._color


# Create an object of class Car
my_car = Car("red")

# Accelerate the car
my_car.accelerate(50)

# Get the current speed
print(f"Current speed: {my_car.get_speed()} km/h")

# Brake the car
my_car.brake(20)

# Get speed after braking
print(f"Speed after braking: {my_car.get_speed()} km/h")

# Change and get the color of the car
my_car.set_color("blue")
print(f"Car color: {my_car.get_color()}")
