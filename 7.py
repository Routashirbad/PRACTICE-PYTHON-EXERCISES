"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
"""

#SOLUTION:

my_list = list(input("Enter your numbers: ")) #Prompt for user to provide numbers for list.

def selected_elements(my_list):
  new_list = list(my_list[0] + my_list[-1]) #Constructing list according to question.
  return new_list

selected_elements(my_list)
