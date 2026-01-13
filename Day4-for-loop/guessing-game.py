from random import randint 
for i in range(1,5):
    guessingNumber = int(input("Guess the number "))
    randomNumber = randint (1,20 )
    if guessingNumber==randomNumber:
        print("You have won ")
    else:
        print("You lose the game")
    print("The random number is",randint(1,20))