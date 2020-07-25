import random
def hangman():
    word=random.choice(["pugger","little","tiger","superman","thor","pokemon","avengers","savewater"])
    validLetters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    while len(word)>0:
        main=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main=main + letter
            else:
                main=main+"_"+" "
        if main==word:
            print(main)
            print("You win!")
            break

        print("Guess The Word: ",main)
        guess=input()


        if  guess in validLetters:
            guessmade=guessmade + guess
        else:
            print("Enter the valid Letter: ")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print(" ---------- ")
            if turns==8:
                print("8 turns left")
                print(" ---------- ")
                print("     O      ")
            if turns==7:
                print("7 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
            if turns==6:
                print("6 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns==5:
                print("5 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns ==4:
                print("4 turns left")
                print(" ---------- ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns ==3:
                print("3 turns left")
                print(" ---------- ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns ==2:
                print("2 turns left")
                print(" ---------- ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns ==1:
                print("1 turns left")
                print("Last Breath Counting ,TAKE CARE")
                print(" ---------- ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns==0:
                print("You Loose")
                print("You let the kind man Die")
                print(" ---------- ")
                print("     O_|    ")
                print("    /|\     ")
                print("    / \     ")
                break

name=input("Enter your Name: ")
print("Welcome" , name)
print("******************")
print("Try to guess the Word in less than 10 try")
hangman()
print()
