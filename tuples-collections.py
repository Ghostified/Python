#tuple = collection which is ordered and unchangable used to grouping related data

student = ("bro",21, "male")
print(student.count("Bro"))
print (student.index("male"))

#iterate over a tuple
for x in student:
    print(x)

#Check if an item exists in a tuple
if "bro" in student:
    print("bro is here")

