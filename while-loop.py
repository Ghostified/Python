#while loop = a statement that will execute a block of code
#               as long as the condition remains true

name = ""

while len(name) == 0:
     name = input("Enter your name: ")

print("Hello " + name)

name2 = None
while not name2:
    name2 = input("Enter your name")
print("Hello " + name2)
