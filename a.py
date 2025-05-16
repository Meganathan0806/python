from abc import ABC,abstractmethod
class Vehicle(ABC):
    @staticmethod
    @abstractmethod
    def engine():
        pass
class Bike(Vehicle):
    @staticmethod
    def engine():
        print("start")
class Car(Vehicle):
    @staticmethod
    def engine():
        print("start")

Car.engine()