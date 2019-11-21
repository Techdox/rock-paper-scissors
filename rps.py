import random

def main():
    if userChoice == "r":
        choiceR()
    elif userChoice == "p":
        choiceP()
    elif userChoice == "s":
        choiceS()
    else:
        print("Error.")

def choiceR():
    if userChoice == "r" and choice == "r":
        print("You Tied")
    elif userChoice == "r" and choice == "p":
        print("You lose")
    elif userChoice == "r" and choice == "s":
        print("You Win!")
    else:
        print("Error.")

def choiceP():
    if userChoice == "p" and choice == "p":
        print("You Tied")
    elif userChoice == "p" and choice == "s":
        print("You lose")
    elif userChoice == "p" and choice == "r":
        print("You Win!")
    else:
        print("Error.")

def choiceS():
    if userChoice == "s" and choice == "s":
        print("You Tied")
    elif userChoice == "s" and choice == "r":
        print("You lose")
    elif userChoice == "s" and choice == "p":
        print("You Win!")
    else:
        print("Error.")

if __name__ == "__main__":
    while True:
        rps = ["r", "p", "s"]
        choice = random.choice(rps)
        userChoice = input("Select [R]ock, [P]aper, or [S]cissors: ").lower()
        main()

        
