#list = used to store multiple items in a single variable

food = ['pizza', 'pepperoni', 'hot dogs', 'pasta']
print(food)
print(food[-1])

#Replace item at an index
food[0] = "sushi"



food.append("ice-cream")
food.remove("hot dogs")
food.pop()
food.insert(0, "Cakes")
food.sort()

for i in food:
    print(i)