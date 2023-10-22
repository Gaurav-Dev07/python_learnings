class Person:
    def __init__(self) -> None:
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    

person1 = Person()
print(person1)
person1.set_name("gaurav")
print(person1.get_name())

person2 = Person()
person2.set_name("dushyant")
print(person2.get_name())