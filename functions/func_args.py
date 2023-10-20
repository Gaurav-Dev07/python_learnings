# *args
# this is use to pass any number of arguments to the python function
def print_args(*args):
    print(args[0])

print_args("oranges","apple","wood")

# **kwargs
def print_kwargs(**kwargs):
    print('name: ',kwargs['name'])
    print('branch: ',kwargs['branch'])

print_kwargs(name="gaurav",branch = "it")

# def print_gauravs(**gaurav):
#     print('name: ',gaurav['name'])
#     print('branch: ',gaurav['branch'])

# print_gauravs(name="gaurav",branch = "it")