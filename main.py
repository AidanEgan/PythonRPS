#rock paper scissors
import random
triFecta = ['r','p','s']
answers = ["DRAW!","YOU LOSER","YOU WIN"]
while True:
    userInput = input("Do you choose rock, paper, or scissors? ").lower()[0]
    if userInput not in triFecta:
        continue
    userFinalChoice = [x for x in range(len(triFecta)) if userInput == triFecta[x]][0]
    comChoice = random.randint(0,2)
    print([answers[y] for y in range(3) if(triFecta[comChoice-y] == triFecta[userFinalChoice])][0])
    if input("Do you want to play again? ").lower()[0] != 'y':
        print("Play again soon")
        break
