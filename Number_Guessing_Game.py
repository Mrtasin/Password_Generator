import random

def Number_Guess_Game():
    num = random.randrange(100)
    print("Welcome to Number Guessing Game...!")
    print("Your Guessing under 100 numbers")
    print("You got 5 opportunity for wining this game")
    for time in range(1,6):
        print("-------------------------------------------\n")
        guess_num = int(input(f"{time} Opportunity, Enter Guessing Number : "))
        if num == guess_num:
            print("You Win this game {} opportunity".format(time))
            break
        elif time == 5:
            print("oops you loss this game,")
            print("Beter luck Next time....!")
        elif num > guess_num:
            print("You Guess Lowest value,\nGuess Highest value")
        elif num < guess_num:
            print("You Guess Highest value,\nGuess Lowest value")


Number_Guess_Game()

