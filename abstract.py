from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Sound Dog ...."


class Cat(Animal):
    def sound(self):
        return "Sound Cat ...."


dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
