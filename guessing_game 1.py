import random

def startGame():
    secret_number = random.randrange(1, 101)
    guess = 0
    attempts = 0
    print("Welcome to the Number Guessing Game")
    name = input("What is your name?  ")
    print("Hi {}, In this game you have to Guess the number between 1 and 100 ".format(name))
    while guess != "A":
        try:
            guess = int(input("Enter the guess\n"))
            attempts += 1
            if guess < 1:
                print("Sorry, invalid value. Guess the number between 1 and 100")
            elif guess > 100:
                print ("Sorry, invalid value. Guess the number between 1 and 100")
            if guess > secret_number:
                print("Guess should be a lower number")
            elif guess < secret_number:
                print("Guess should be a higher number")
            else:
                print("Congratulations ! You got it")
                print("The total number of attempts are {}.".format(attempts))
                print("Game Over!\nGood Bye till next time")
                break
        except ValueError:
            print("Sorry, This is a invalid value. Please try again")
        else:
            continue

if __name__ == '__main__':
    startGame()
