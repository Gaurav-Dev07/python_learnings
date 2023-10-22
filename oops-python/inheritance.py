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
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        
emp_1 = Employee("gaurav","shukla",50000)
emp_2 = Employee("axat","bhardwaj",100000)

# inheritance
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, f_name, l_name, pay, prog_lang) -> None:
        # calling the parent's constructor and passing the arguments
        super().__init__(f_name, l_name, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("gaurav","dev",50000,'python')
dev_2 = Developer("axat","dev",200000,'java')

print("dev1 email -> ", dev_1.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

class Manager(Employee):
    def __init__(self, f_name, l_name, pay,employees = None) -> None:
        super().__init__(f_name, l_name, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp)

manager = Manager("kiran","shahpur",2500000,["pravalika","sahithi","devesh"])
manager.print_emps()
manager.add_employee("gaurav")
print("-------employee added-----------")
manager.print_emps()
manager.remove_employee("gaurav")
print("-------employee removed---------")
manager.print_emps()

