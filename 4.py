"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""


#SOLUTION:

import random

a = random.randint(1,10)
guess = 0
c = 0
while guess != a and guess != "exit":
    guess = input("Enter a guess between 1 to 9: ")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess == a :
      print("Exactly right guess !")
    elif guess > a :
      print("Too high mate !")
    elif guess < a:
      print("Too low mate !")
    else:
          print("Right!")
          print("You took only", c, "tries!")
