'''
CS1030-10809
Name: Austin Leavitt
700#: 7006611930
Assignment / Problem#:
Description: rock paper scissors; play continuosly until player or computer wins
more than two times

'''
#import random module
import random

#counters for player and computer wins
playerWins = 0
computerWins = 0

#variable for storing whether the player won. 0 = tie 1 = won 2 = loss
playerWon = 0

#play game until either player or computer has more than 2 wins
while playerWins < 3 and computerWins < 3:

    #generate random play for the computer
    computerPlay = random.randint(0,2)

    playerPlay = eval(input("scissor (0), rock(1), paper(2): "))
    #scissors cases
    if playerPlay == 0:
        if computerPlay == 1:
            playerWon = 2
        elif computerPlay == 2:
            playerWon = 1
        else:
            playerWon = 0
    #rock cases
    elif playerPlay == 1:
            if computerPlay == 1:
                playerWon = 0
            elif computerPlay == 2:
                playerWon = 2
            else:
                playerWon = 1
    #paper cases
    elif playerPlay == 2:
            if computerPlay == 1:
                playerWon = 2
            elif computerPlay == 2:
                playerWon = 0
            else:
                playerWon = 1

    #ouput results of the round and increment wins if neccessary
    if computerPlay == 0:
        print("The computer is scissor.", end = " ")
    elif computerPlay == 1:
        print("The computer is rock.", end = " ")
    else:
        print("The computer is paper.", end = " ")

    if playerPlay == 0:
        print("You are scissor", end = " ")
    elif playerPlay == 1:
        print("You are rock", end = " ")
    else:
        print("You are paper", end = " ")

    if playerWon == 0:
        print("too. It is a draw.")
    elif playerWon == 1:
        print(". You won.")
        playerWins += 1
    else:
        print(". You loose.")
        computerWins +=1
    #output the win count
    print(f"Player: {playerWins} Computer: {computerWins}")
    print()

#Output the result of the entire game
if playerWins > 2:
    print("You won the match!")
else:
    print("Computer won the match. Better luck next time!")
