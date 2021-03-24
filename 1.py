"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""

#SOLUTION:

My_String = str(input("Enter a string: ")) #Prompt for user to give a string.

if My_String[::-1] == My_String:
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
