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

    # using class methods we can recieve class as the first argument instead of instance
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first ,last ,pay = emp_str.split('-')
        return Employee(first,last,pay)
    
    # static method
    # doesn' takes any instance or class as argument
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        
emp_1 = Employee("gaurav","shukla",50000)
emp_2 = Employee("axat","bhardwaj",100000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

emp_str_1 = "john-doe-9000"
emp_str_2 = "akash-sharma-15000"
emp_str_3 = "shivansh-bhatnagar-299999"

# using class method
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)