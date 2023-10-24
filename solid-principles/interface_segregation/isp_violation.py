# interface segregation principle states that class should not implement interface which the don't use

from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,name,department):
        self.name = name
        self.department = department
    
    @abstractmethod
    def attend_standup(self):
        pass

    @abstractmethod
    def pr_review(self):
        pass

    def print_info(self):
        print("employee name " + self.name + " department is " + self.department)

class Developer(Employee):
    def __init__(self,name,department):
        super().__init__(name,department)

    def attend_standup(self):
        print("dev giving standup")

    def pr_review(self):
        print("working on pr review")

class Manager(Employee):
    def __init__(self,name,department):
        super().__init__(name,department)

    def attend_standup(self):
        print("manager taking standup")

    # this manager class does not needs this method this violates interface segregation principle
    def pr_review(self):
        print("manager doesn't do pr reviews")

    
    
dev = Developer("gaurav","engineering")
dev.print_info()

manager = Manager("shivani","product management")
manager.print_info()