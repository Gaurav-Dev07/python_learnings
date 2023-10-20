# function with normal parameter
def add(val_a,val_b):
    return val_a + val_b

print(add(5,19))

# function with defaul parameter
def add_default(val_a,val_b = 10):
    return val_a + val_b

print(add_default(5))

# function with default arguments
def add_arguments(val_a,val_b):
    print("val_a = ",val_a)
    print("val_b = ",val_b)
    return val_a + val_b
# if you define values while calling the function then you don't require to pass arguments in correct order

print(add_arguments(val_a=10,val_b=67))
print(add_arguments(val_b=10,val_a=5))