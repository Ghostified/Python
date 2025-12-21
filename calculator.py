# num1 = float(input("Enter a number"))
# num2 = float(input("Enter another number"))
# sum = num1 + num2
# print(sum)

#Madlibs
# color = input ("Enter a color: ")
# plural_noun = input ("Enter a plural noun: ")
# celebrity = input ("Enter a celebrity: ")
#
# print("Roses are " + color)
# print ( plural_noun + " are blue")
# print("I love " + celebrity)

#List - used to list of information
number = [4,5,6,7,8,9,10,43,21,43,44,54,63,31]
food = ["Cake", "Meat Balls","Tea", "Tea"]
for i in food:
    print(i)

print(food[0])
#food.extend(number)
food.append("Coffee")
food.insert(2,"Biscuits")
print(food)
food.pop()
print(food)

#Check if an element is in the list
print(food.index("Tea"))
print(food.count("Tea"))
number.sort()
print(number)
number.reverse()
print(number)

