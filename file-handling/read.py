# Python code to illustrate read() mode
file = open("geeks.txt", "r") 
print (file.read())


with open("geeks.txt","r") as geek_file:
    # print(geek_file.read())
    print("printing lines in loop")
    for line in geek_file:
        print("line => ",line)