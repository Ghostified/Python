#logical operators (and, or, not)  = used to check if two or more conditional statements are

temp = int(input("What is the temprature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temprature is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30):

    print("its averagely warm")
    print("Go outside!")
else:
    print("Its not warm outside")
