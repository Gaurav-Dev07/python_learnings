fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0])

# loops in tuples
for fruit in fruits:
    print("fruit = ", fruit)

print(fruits[-1])

# way of applying some methods of list in tuples
y = list(fruits)
y.append("orange")
thistuple = tuple(y)

print(thistuple)