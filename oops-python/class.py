class Employee:
    # constructor
    # each method in python class takes the first argument as instance as we can see here and other methods
    def __init__(self,f_name,l_name) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.email = f_name + '.' + l_name + '@company.com'

    # method
    def get_fullname(self):
        return f"{self.f_name} {self.l_name} "
        
emp_1 = Employee("gaurav","shukla")
emp_2 = Employee("axat","bhardwaj")

print(emp_1.email)
print(emp_2.email)
print("------------------fullname-------------------")
# when we call method like this emp_1's instance will directly go as argument in this functin method call
print(emp_1.get_fullname())
