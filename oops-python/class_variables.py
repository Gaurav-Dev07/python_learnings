class Employee:

    # class variable
    raise_amount = 1.04
    num_of_emps = 0

    # constructor
    # each method in python class takes the first argument as instance as we can see here and other methods
    def __init__(self,f_name,l_name,pay) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.pay = pay
        self.email = f_name + '.' + l_name + '@company.com'

        Employee.num_of_emps += 1
        
    # method
    def get_fullname(self):
        return f"{self.f_name} {self.l_name} "
    
    def apply_raise(self):
        self.pay  = (self.pay * self.raise_amount)
        
emp_1 = Employee("gaurav","shukla",50000)
emp_2 = Employee("axat","bhardwaj",100000)

print(emp_1.email)
print(emp_2.email)
print("------------------fullname-------------------")
# when we call method like this emp_1's instance will directly go as argument in this functin method call
print(emp_1.get_fullname())

print(emp_1.pay)
print("pay after raise")
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.num_of_emps)