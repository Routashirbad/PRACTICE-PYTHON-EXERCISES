"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

#SOLUTION:

x = "Player 1 wins!! :))"
y = "Player 2 Wins!! :))"
z = "Its a draw !! :(("
while True:
  a = input("Player 1 choice: ").lower()
  b = input("Player 2 choice: ").lower()
  if ((a == 'rock' and b == 'scissors') or (a == 'scissors' and b == 'paper') or (a == 'paper' and b == 'rock')) :
    print(x)
    break
  elif ((a == 'scissors' and b == 'rock') or (a == 'paper' and b == 'scissors') or (a == 'rock' and b == 'paper')):
    print(y)
    break
  elif ((a == 'scissors' and b == 'scissors') or (a == 'paper' and b == 'paper') or (a == 'rock' and b == 'rock')):
    print(z)
    break
  else:
    print('Mistype Error')
    check = input('Press yes to play again: ').lower()
    if (check == 'yes'):
      continue
    else:
      break

