
import random
import requests

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
word = random.choice(WORDS).decode('UTF-8')
# code for hangman

tmp = list("_" * len(word)) 

# checks if letter is in word
#returns false if not

def in_word(x):
    if x in word:
        return True
    else:
        return False    


def hangman(guesses):

    if guesses == 4:
        print("________")
        print("|       |")
        print("|       |")
        print("|     (-_-)")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("__       ")
    
    if guesses == 3:
        print("________")
        print("|       |")
        print("|       |")
        print("|     (-_-)")
        print("|     __|__")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("__       ")

    if guesses == 2:
        print("________")
        print("|       |")
        print("|       |")
        print("|     (-_-)")
        print("|     __|__")
        print("|       |")
        print("|        ")
        print("|        ")
        print("|        ")
        print("__       ")

    if guesses == 1:
        print("________")
        print("|       |")
        print("|       |")
        print("|     (-_-)")
        print("|     __|__")
        print("|       |")
        print("|       /")
        print("|        ")
        print("|        ")
        print("__       ")
        
    if guesses == 0:
        print("________")
        print("|       |")
        print("|       |")
        print("|     (X_X)")
        print("|     __|__")
        print("|       |")
        print("|       /\\")
        print("|        ")
        print("|        ")
        print("__       ")

def print_word(x):

    for c in x:
        for i in range(len(word)):
            if(c == word[i]):
                tmp[i] = c

    for i in tmp:
        print(i + " ", end = " ")

    print("")
    return 

def game_check():

    game_over = 1
    for i in tmp:
        if i == '_':
            game_over = 0

    return game_over
        
def guess(x):
    guesses = x*x

    print("________")
    print("|       |")
    print("|       |")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("__       ")

    

    guessed = "You've guessed: "
    correct = " "
    print("You have " + str(guesses) + " guess(es)")

    while guesses != 0:
        print_word(correct)
        if game_check() == 1:
            print("Well Done! You Win :D")
            break
        print("")
        char = input("Guess a letter: ")
        print("------------------------")
        if(len(char) == 1):
            if(in_word(char) == True):
                print("correct!")
                correct += char
                if game_check() == 1:
                    print("Well Done! You Win :D")
                    break
            else:
                
                if char not in guessed:
                    guessed += char
                
                guesses = guesses - 1
                print("Wrong! You have " + str(guesses) + " guesses left")
                hangman(guesses)
        
        else:
            if(char == word):
                correct += char
                
                

            else:
                guesses = guesses - 1
                print("Wrong! You have " + str(guesses) + " guesses left")
                hangman(guesses)
        
        print(guessed)

    if game_check() == 0:
        print("No guesses left, you lose.")
        print("The word was: " + word)
        print("------------------------")

    return

def main():
    print("------------------------")
    print("Welcome to hangman!")
    print("Extreme: 1, Hard: 2, Medium: 3, Easy: 4, Super Easy: 5")
    x = int(input("Select a difficulty: "))
    guess(x)

    return



main()
   
