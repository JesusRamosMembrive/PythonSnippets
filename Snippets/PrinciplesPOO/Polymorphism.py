"""
@Author: Jesus Ramos Membrive
@Date: 25/11/2023
@Link: ramos.membrive@gmail.com
@Description:
 Polymorphism in object-oriented programming allows objects of different classes to be treated as objects of a common
 superclass. It's particularly useful for implementing functions or methods that can operate on objects
 of different classes.
"""
from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"


def animal_sound(animal):
    """ Function to demonstrate polymorphism """
    print(animal.speak())


# Creating instances of different classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Chirpy")

# Demonstrating polymorphism
animal_sound(dog)  # Outputs: Buddy says Woof!
animal_sound(cat)  # Outputs: Whiskers says Meow!
animal_sound(bird)  # Outputs: Chirpy says Tweet!


# Another example with abstract classes

class AbstractClass(ABC):

    @abstractmethod
    def representation(self):
        pass


class Example1(AbstractClass):
    def __init__(self, parameter):
        self.parameter = parameter

    def representation(self):
        return f"{self.parameter} from example 1!"


class Example2(AbstractClass):
    def __init__(self, parameter):
        self.parameter = parameter

    def representation(self):
        return f"{self.parameter} from example 2!"


class Example3(AbstractClass):
    def __init__(self, parameter):
        self.parameter = parameter

    def representation(self):
        return f"{self.parameter} from example 3!"


command = 2
example = None
match command:
    case 1:
        example = Example1("Hello")
    case 2:
        example = Example2("Hello")
    case 3:
        example = Example3("Hello")
    case _:
        print("Invalid command")

print(example.representation())  # Outputs: Hello from example 1!
