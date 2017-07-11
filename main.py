#rock paper scissors
import random
triFecta = ['r','p','s']
while True:
    userInput = input("Do you choose rock, paper, or scissors? ").lower()[0]
    if userInput not in triFecta:
        continue
    userFinalChoice = [x for x in range(len(triFecta)) if userInput == triFecta[x]][0]
    comChoice = random.randint(0,2)
    if (triFecta[comChoice-2] == triFecta[userFinalChoice]):
        print ("YOU WIN!")
    elif (triFecta[userFinalChoice-2] == triFecta[comChoice]):
        print ("YOU LOSER")
    else:
        print ("DRAW!")
    if input("Do you want to play again? ").lower()[0] != 'y':
        print("Play again soon")
        break
