"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

#SOLUTION:

str1 = str(input("Write a line : "))

def cop(str1):
  str2 = str1.split()
  str3 = str2[::-1]
  str4 =" ".join(str3)
  print(str4)

cop(str1)
