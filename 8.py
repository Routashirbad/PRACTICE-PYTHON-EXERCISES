"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

#SOLUTION:

l=int(input('Enter length for list: '))

def fibo_nums(a):
  list1=[None]*a
  list1[0]=1
  list1[1]=1
  for i in range(2,a):
    list1[i]=int(list1[i-1])+int(list1[i-2])
  return list1

print (fibo_nums(l))
