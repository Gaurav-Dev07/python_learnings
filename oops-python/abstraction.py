from abc import ABC, abstractmethod

class Car(ABC):
    
    # this method should be defined in subclass
    @abstractmethod
    def start(self):
        pass

# concrete subclass Electric Car
class ElectricCar(Car):
    def start(self):
        print("starting the electric motor..ready to drive")

# concrete subclass DeiselCar
class DeiselCar(Car):
    def start(self):
        print("starting the deisel engine..ready to drive")

electric_car = ElectricCar()
deisel_car= DeiselCar()
electric_car.start()
deisel_car.start()
