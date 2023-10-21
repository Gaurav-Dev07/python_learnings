# set stores unique values
my_set = {1,2,4,5,6,6}
print(my_set)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# add set items
thisset.add("orange")
thisset.add("orange")
print(thisset)
thisset.remove("apple")
print(thisset)
thisset.pop()
print(thisset)