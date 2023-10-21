my_tuple = ("apple","banana","orange")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[0:2])
print(my_tuple[-1])

# update tuples
list_my_tuple = list(my_tuple)
list_my_tuple.append("guava")
my_tuple = tuple(list_my_tuple)
print("updated = ",my_tuple)

# unpack tuples
(item1,item2,item3,item3) = my_tuple
print("item1 = ",item1)
print("item2 = ",item2)
print("item3 = ",item3)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# loop tuples
for fruit in fruits:
    print("fruits -> ",fruit)