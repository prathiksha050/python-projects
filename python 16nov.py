p1 = input("Player 1 (rock, paper, scissor): ")
p2 = input("Player 2 (rock, paper, scissor): ")
if p1==p2:
  print("draw")
elif p1 == "rock" and p2 == "scissor":
  print("Player 1 wins")
elif p1 == "paper" and p2 == "rock":
  print("Player 1 wins")
elif p1 == "scissor" and p2 == "paper":
  print("Player 1 wins")
elif p1 == "scissor" and p2 == "rock":
  print("Player 2 wins")
elif p1 == "rock" and p2 == "paper":
  print("Player 2 wins")
elif p1 == "paper" and p2 == "scissor":
  print("Player 2 wins")
else:
  print("Invalid")




min = 1
max = 100
print("Guess a number between 1 to 100")

while True:
  guess = (min + max) // 2
  print("My guess is", guess)
  ans = input("Enter yes or greater or lesser: ")
  
  if ans == "yes":
    print("right guess")
    break
  elif ans == "greater":
    min = guess + 1
  elif ans == "lesser":
    max = guess - 1
  else:
    print("invalid")
