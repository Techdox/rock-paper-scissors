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
    if choice == "r":
        print("You Tied")
    elif choice == "p":
        print("You lose")
    elif choice == "s":
        print("You Win!")
    else:
        print("Error.")

def choiceP():
    if choice == "p":
        print("You Tied")
    elif choice == "s":
        print("You lose")
    elif choice == "r":
        print("You Win!")
    else:
        print("Error.")

def choiceS():
    if choice == "s":
        print("You Tied")
    elif choice == "r":
        print("You lose")
    elif choice == "p":
        print("You Win!")
    else:
        print("Error.")

if __name__ == "__main__":
    while True:
        rps = ["r", "p", "s"]
        choice = random.choice(rps)
        userChoice = input("Select [R]ock, [P]aper, or [S]cissors: ").lower()
        main()

        
