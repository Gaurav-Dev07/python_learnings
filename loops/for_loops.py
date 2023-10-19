# ----------------------------------------------SYNTAX-------------------------------------------
# for iterator_var in sequence:
#     statements(s)



# ------------------LOOPING IN RANGE-------------------------
print("\n------------------LOOPING IN RANGE-------------------------\n")
n = 5
for i in range(0,n):
    print("i = ",i)

# ------------------LOOPING IN LIST--------------------------
print("\n------------------LOOPING IN LIST--------------------------\n")
list = [1,"gaurav",2,3,4,5]
for item in list:
    print("item = ",item)

# ------------------LOOPING IN STRING------------------------
print("\n------------------LOOPING IN STRING------------------------\n")
text = "Hello"
for char in text:
    print("char = ",char)

# -------------------LOOPING IN DICTIONARY--------------------
print("\n-------------------LOOPING IN DICTIONARY--------------------\n")
person = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}
for key, value in person.items():
    print(key, ":", value)
