print("Rock, paper, scissors...GO!")

tie = 0
userWins = 0
compWins = 0

playAgain = True
while playAgain:
    print("Enter 1 for rock, 2 for paper, or 3 for scissors: ")
    user = input()
    while user != 1 and user != 2 and user != 3:
        print("Invaid entery. Try again: ")
        user = input()
    if user == 1:
        print("You picked rock.")
    elif user == 2:
        print("You picked paper.")
    elif user == 3:
        print("You picked scissors.")

    import random
    computer = random.randint(1, 3)
    if computer == 1:
        print("I picked rock.")
    elif computer == 2:
        print("I picked paper.")
    elif computer == 3:
        print("I picked scissors.")

    if user == 1:
        if computer == 1:
            print("We tied.")
            tie = tie + 1
        elif computer == 2:
            print("I won.")
            compWins = compWins + 1
        elif computer == 3:
            print("You won.")
            userWins = userWins + 1
    elif user == 2:
        if computer == 2:
            print("We tied.")
            tie = tie + 1
        elif computer == 3:
            print("I won.")
            compWins = compWins + 1
        elif computer == 1:
            print("You won.")
            userWins = userWins + 1
    elif user == 3:
        if computer == 3:
            print("We tied.")
            tie = tie + 1
        elif computer == 1:
            print("I won.")
            compWins = compWins + 1
        elif computer == 2:
            print("You won.")
            userWins = userWins + 1

    print(" Do you want to play again? Type 'yes' or 'no'): ")
    userInput = input()
    if userInput == "no":
        playAgain = False
    elif userInput == "yes":
        playAgain = True

print "You won", userWins, "times"
print "I won ", compWins, " times."
print "We tied ", tie," times."

print("End of game...bye!")
