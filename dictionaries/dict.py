# dictionaries are data structures in python which is use to store data in keyvalue pairs
person = {
    "name": "gaurav",
    "age": 24,
    "city": "ghaziabad",
    "qualification": "btech"
}

print("person = ",person)
print("person[name] -> ",person["name"])

# get list of keys
person_keys = person.keys()
print("person_keys -> ",person_keys)
print("person_keys list -> ",list(person_keys))

# getting values of dictionary
person_values = person.values()
print("person_values -> ",person_values)

# add a mew item to dict
person["designation"] = "software dev"
print('person["designation"] -> ',person["designation"])

# updating the dictionaries
person.update({"name": "aniket"})
person["age"] = 12
print("person -> ",person)

# you can also add items in similar way

person.update({"caste": "brahmam"})
person["maritial-status"] = "single"
print("person -> ",person)

# removing items 
# this will remove items from the last
person.popitem()
print("person -> ",person)

# this will remove specifeid key
person.pop("age")
print("person -> ",person)

# remove from del
del person["city"]
print("person -> ",person)
# removes the whole dictionary from memory


# loops in dictionary
for key, val in person.items():
    print("key: ",key, ", val: ",val)

for key, val in person.items():
    print("key: ",key, ", val: ",val)