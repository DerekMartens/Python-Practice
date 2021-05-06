import random

def loadWords():
    words = []
    f = open("Hangman\words.txt", "r")
    for line in f:
        words.append(line.strip("\n"))
    f.close()
    return words

def generateBlankedWord():
    generateBlankedWord = []
    for i in selectedWord:
        generateBlankedWord.append("_")
    return generateBlankedWord

def updateGuessedWord(guessedWord):
    for i, c in enumerate(selectedWord):
        if c == newLetter:
            guessedWord[i] = c
    return guessedWord

def toString(inputList):
    retVal = ""
    for ele in inputList:
        retVal += ele
    return retVal

def verifyLetter(letter):
    notVerified = True
    while notVerified:
        if len(letter) == 1 and letter.isalpha():
            notVerified = False
        else:
            letter = input("Please enter a single letter: ")
    return letter




MAX_GUESSES = 12
guesses = 0
complete = False
guessedLetters = []
selectedWord = ""
guessedWord = ""
newLetter = ''

#START OF GAME
print("Welcome to Hangman")
print("Let's play a game, You guess the word I've chosen")
output = "The default number of guesses is {}, Would you like to change it? (y/n)"
val = input(output.format(MAX_GUESSES))
if val == 'y':
     val = input("Enter your desired number of turns: ")
     if val.isnumeric(): 
         MAX_GUESSES = int(val)
output = "Okay, you have {} guesses!"
print(output.format(MAX_GUESSES))

words = loadWords()
selectedWord = words[random.randint(0,len(words) - 1)]
guessedWordList = generateBlankedWord()
guessedWord = toString(guessedWordList)

while guesses < MAX_GUESSES and not complete:
    print()
    print("Here's the word so far")
    print(guessedWord)
    guesses += 1

    newLetter = verifyLetter(input("Guess a leter: "))
    guessedLetters.append(newLetter)
    print("Thank you, Here are the letters you've guessed so far:")
    print(guessedLetters)

    updateGuessedWord(guessedWordList)
    guessedWord = toString(guessedWordList)

    if guessedWord == selectedWord:
        print("Congrats, you got the word!")
        complete = True
else:
    print("The word was " + selectedWord)
    print("Wanna play again?!")
