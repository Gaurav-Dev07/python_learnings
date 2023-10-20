branches = ['cs','it','ec','mechanical','civil']
branches[0]
print(branches[0])
print(branches[0:3])
print(branches[:4])
print(branches[4:])

# print from last
print(branches[-1]);

# check item in list
if ('cs' in branches):
    print("present")

# adding items in list
branches.append('metallurgy')

print(branches)

# insert an item at a position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove a particular item from list
thislist.remove("apple")
print(thislist)

# remove an item from a particular index
thislist.pop(2)
print(thislist)

# remove the last item
thislist.pop()
print(thislist)

# looping list
cars = ['audi','mercedes','bmw']

for i in range(len(cars)):
    print("i = ",i)
    print("cars[i] = ", cars[i])

