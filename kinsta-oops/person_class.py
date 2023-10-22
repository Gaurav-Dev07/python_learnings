class Person:
    # constructor of python object
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name : {self.name}, age: {self.age}")

# object initialization
person1 = Person("gaurav",25)
print("name -> ",person1.name)
print("age -> ",person1.age)
person1.display_info()