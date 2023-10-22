# method overloading

class Calculor:
    def add_numbers(self, first,second = None,third = None):
        if second is not None and third is not None:
            return first + second + third
        elif second is not None:
            return first + second
        else:
            return first + 0
        
    

calci = Calculor()
print(calci.add_numbers(10))
print(calci.add_numbers(10,15))
print(calci.add_numbers(2,3,4))

# method overriding
class Animal:
    def sound(self):
        print("generic animal sound")

class Cat(Animal):
    def sound(self):
        print("meow meow..")

class Dog(Animal):
    def sound(self):
        print("bhow bhow...")

animal = Animal()
cat = Cat()
dog = Dog()

animal.sound()
dog.sound()
cat.sound()