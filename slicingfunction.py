#Slicing = Create a substring by extracting elements from another string
#           indexing [] or slice ()
#           [start: stop:step]

"""
    name = "Branson Allan"
    first_name = name[0 : 9]
    last_name = name [8:]
    print(first_name)
    print(last_name)

    funky_name = name[::3]
    print(funky_name)

    resversed_name = name[::-1]
    print(resversed_name)
"""

website1 = "https://www.youtube.com"
website2 = "https://www.wikipedia.com"
slice = slice(12,-4)
print(website1[slice])
print(website2[slice])
