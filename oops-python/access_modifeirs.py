# public
class MyClass:
    def my_method(self):
        print("my method")
myclass = MyClass()

myclass.my_method()

# protected
class MyAccount:
    def __init__(self) -> None:
        self._balance = 50000
    
    def _get_balance(self):
        return self._balance
    
account = MyAccount()
print(account._balance)
print("getting balance", account._get_balance())
        
# private class
class MyClass:
    def __init__(self):
        self.__private_variable = 30

    # private methods definitionn they should not be used outside class
    def __private_method(self):
        print("This is a private method.")

obj = MyClass()
# this is a private method so we cannot access it outside the class
# obj.__private_method()


