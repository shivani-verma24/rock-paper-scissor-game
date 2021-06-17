import random
from logo import rock, paper, scissors

game = [rock, paper, scissors]
u = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))
if (u > 2):
    print("Invalid number")
else:
    print(game[u])
    c = random.randint(0, 2)
    print("Computer chose: \n")
    print(game[c])

    if (u == 0 and c == 2):
        print("You win")
    elif (u == 2 and c == 0):
        print("You lose")
    elif (c > u):
        print("You lose")
    elif (u > c):
        print("You win")
    elif (u == c):
        print("It's a draw.")


# Project by Shivani Verma