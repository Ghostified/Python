#Function to emasure how long a  functuin takes to run

import timeit

#Implementation 1 : list compression
code1 = " "
a = [1,2,3.4,5]
b = [x * 2 for x in a ]

time1 = timeit.timeit(code1, number = 100000)

printf(f"list compression time: {time1}")