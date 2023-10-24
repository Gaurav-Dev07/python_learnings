# solution - build different interface for different classes which serves the ultimate purpose
from abc import ABC, abstractmethod

class DevTasks(ABC):
    def __init__(self,name,department):
        self.name = name
        self.department = department

    @abstractmethod
    def pr_review(self):
        pass

    @abstractmethod
    def update_tickets(self):
        pass
    
    @abstractmethod
    def integrate_apis(self):
        pass

    @abstractmethod
    def build_apis(self):
        pass

class ManagerTasks(ABC):
    def __init__(self,name,department):
        self.name = name
        self.department = department

    @abstractmethod
    def take_standup(self):
        pass
    @abstractmethod
    def track_jira(self):
        pass
    @abstractmethod
    def sprint_planning(self):
        pass

class Developer(DevTasks):
    def __init__(self,name,department):
        super().__init__(name,department)
    
    def pr_review(self):
        print("doing pr reviews")

    def integrate_apis(self):
        print("integrating apis")
    
    def build_apis(self):
        print("building apis")
    
    def update_tickets(self):
        print("updating tickets")

    

class Manager(ManagerTasks):
    def __init__(self,name,department):
        super().__init__(name,department)
    
    def take_standup(self):
        print("taking standup")
    
    def track_jira(self):
        print("tracking jira tickets")

    def sprint_planning(self):
        print("planning sprint") 
    
    
dev = Developer("gaurav","engineering")
dev.pr_review()
dev.integrate_apis()
dev.build_apis()
print("---------------------------------------")
manager = Manager("shivani","product management")
manager.take_standup()
manager.track_jira()
manager.sprint_planning()