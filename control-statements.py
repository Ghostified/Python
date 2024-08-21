#loop control statements = change a loops execution normal sequence

#break = used erminate the entire loop
#continue = skips to the next iteration of the loop
#pass = does nothing, acts  place holder

#Break Example

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# #This program skips the under score value in the phone number variable
# phone_number = "1234_456_789"
#
# for i in phone_number:
#     if i == "_":
#         continue
#     print(i, end="")

#Pass does nothing
for i in range(20+ 1):
    if i == 13:
        pass
    else:
        print(i, end="")