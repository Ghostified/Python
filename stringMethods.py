name = "ghost"
sudo = "BRANSON"

#Prints the length of the string
print(len(name))

#Find Method
print(name.find("o")) #Returns the index of the character
print(name.find("s"))

#Capitalize Method returns the first index of the string in upper case
print(name.capitalize())

print(sudo.lower())
print(name.upper())
print(name.islower())
print(name.isdigit())
print(sudo.isalpha()) #Used to check if a string only contains alphabets
print(name.count("o"))
print(name.replace("g", "t"))

#Display a string multiple times by multiplying the string multiple time
print(sudo*5)