#if statement = a block  of code that will execute if the condition is true

age = int(input("How old are you? :  "))

if age >= 18 | age <= 99:
    print("You are an adult!")
elif age == 100:
    print("You are an octogenarian!")
elif age < 0:
    print("You are yet to be born")
else:
    print("You are not old enough")

