class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass  # Abstract method to be implemented by subclasses

#These classes are concrete implementations of the Vehicle abstract base class.
class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

#This is an abstract base class that defines the factory method.
class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass  # Abstract factory method to create a vehicle

# These classes are concrete implementations of the VehicleFactory abstract base class.
class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()

