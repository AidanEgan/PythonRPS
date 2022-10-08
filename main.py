#rock paper scissors
import random
triFecta = ['r','p','s']
getInput = lambda inputStr, message="": (theInput[0] if theInput else getInput(inputStr, print("I need a response!"))) if (theInput := input(inputStr).lower()) else getInput(inputStr, print("I need a response!"))
while triFecta:
    userInput = getInput("Do you choose rock, paper, or scissors? ")
    userFinalChoice = [x for x in range(len(triFecta)) if userInput == triFecta[x]][0] if userInput in triFecta else -1
    userFinalChoice = (print([["DRAW!","YOU LOSER","YOU WIN"][y] for y in range(3) if (triFecta[userInput-y] == triFecta[userFinalChoice])][0]) if userFinalChoice != -1 else -1) if ((userInput := random.randint(0,2)) != -1) else print("Unreachable!")
    triFecta = (triFecta if (getInput("Do you want to play again? ") == 'y') else print("Play again soon")) if userFinalChoice != -1 else triFecta