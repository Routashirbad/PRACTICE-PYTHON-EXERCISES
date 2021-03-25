"""
Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.
Extra:

Randomly generate two lists to test this
"""

#SOLUTION:

import random

a = random.sample(range(100),8) #Randomly generationg first list
b = random.sample(range(100),11) #Randomly generating second list
Cf = [] #Creating an empty list

for i in a and b : Cf.append(i)
print(list(set(Cf))) #Common values in both the lists.

