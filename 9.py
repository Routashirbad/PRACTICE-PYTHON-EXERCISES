"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

#SOLUTION:


#Duplicating using loop.

a = list((input("Enter a list: ")))

def dupli(a):
  b = []
  for i in a:
    if i not in b:
      b.append(i)
  return b

print("list a is :" , a)
print("duplicate of a is : " , dupli(a))


#Duplication using sets

x = list(input("Enter your list: "))

def s_dupli(x):
    return list(set(x))

print("list x is : ", x)
print(s_dupli(x))


