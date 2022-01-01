draw1 = [
'''
 +---+
     |
     |
     |
    ===
''',
'''
 +---+
 O   |
     |
     |
    ===
''',
'''
 +---+
 O   |
 |   |
     |
    ===
''',
'''
 +---+
 O   |
/|   |
     |
    ===
''',
'''
 +---+
 O   |
/|\  |
     |
    ===
''',
'''
 +---+
 O   |
/|\  |
/    |
    ===
''',
'''
 +---+
 O   |
/|\  |
/ \  |
    ===
''',
'''
 +---+
[O   |
/|\  |
/ \  |
    ===
''',
'''
 +---+
[O]  |
/|\  |
/ \  |
    ===
'''
]

dataset = {'cities' : ['Tokyo', 'New York', 'Mexico City', 'Mumbai',
'Sao Paulo', 'Delhi', 'Shanghai', 'Kolkata', 'Los Angeles',
'Dhaka', 'Karachi', 'Cairo',
'Osaka', 'Beijing', 'Manila', 'Moscow', 'Istanbul', 'Paris', 'Seoul',
'Jakarta','Chicago', 'London', 'Tehran',
'Bogota', 'Shenzhen', 'Wuhan', 'Hong Kong', 'Tianjin', 'Chennai', 'Taipei', 'Bengaluru',
'Bangkok', 'Lahore', 'Miami', 'Hyderabad', 'Dallas', 'Santiago', 'Philadelphia',
'Madrid', 'Houston', 'Ahmadabad', 'Washington', 'Atlanta',
'Toronto', 'Singapore', 'Baghdad', 'Barcelona','Pune','Boston', 'Sydney'],
'colours' : ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black', 'Brown',
'Ivory', 'Teal', 'Silver', 'Purple', 'Magenta', 'Olive', 'Cyan'],
'fruits' : ['Orange', 'Apple', 'Avocado', 'Mango', 'Peach', 'Cherry', 'Grape', 'Banana', 'Watermelon', 'Strawberry', 'Blueberry',
'Guava', 'Raspberry', 'Kiwi','Apricot', 'Pear', 'Fig', 'Lemon', 'Papaya', 'Pomegranate', 'Plum', 'Passion fruit', 'Coconut', 'Lychee']}

import random, copy
def randomWord(dataset):
    catagory = random.choice(list(dataset.keys()))
    return [dataset[catagory][random.randint(0,len(dataset[catagory])-1)], catagory]


def board(correctGuess,missedGuess,secretWord):
    print(draw[len(missedGuess)], end="\n")

    print('Missed Letters:',end = " ")
    for x in missedGuess:
        print(x,end= " ")
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i].lower() in correctGuess:
            blanks = blanks[0:i] + secretWord[i] + blanks[i+1:]

    for x in blanks:
        print(x,end=" ")
    print(f'({catagory})')
    print()

def getGuess(alreadyGuessed):# correcGuess+missedGuess
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Enter a single letter!")
        elif guess in alreadyGuessed:
            print("You have already guessed this letter, try another one!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter an alphabet!")
        else:
            return guess

def playagain():
    answer = input("Do you want to play again(yes or no)?")
    return answer.lower().startswith('y')

correctGuess = ""
missedGuess = ""
secretWord,catagory = randomWord(dataset)
gameisover = False
print(f"HANGMAN")
difficulty = ""
draw = copy.deepcopy(draw1)
while difficulty == "":
    difficulty  = input("Choose (H)ard(4),(M)edium(6) or (E)asy:").upper()
    if difficulty  == 'H':
        del draw[2]
        del draw[2]
        del draw[3]
        del draw[4]
    if difficulty  == "M":
        del draw[3]
        del draw[4]

while True:
    board(correctGuess,missedGuess,secretWord)
    attempt = getGuess(correctGuess + missedGuess)
    if attempt in secretWord.lower():
        correctGuess += attempt
        foundAll = True
        for i in range(len(secretWord)):
            if secretWord[i].lower() not in correctGuess:
                foundAll = False
                break
        if foundAll:
            print(f"Yay! The secret word is {secretWord}. You have won!")
            gameisover = True
    else:
        missedGuess += attempt
        if len(missedGuess) == len(draw) - 1:
            board(correctGuess,missedGuess,secretWord)
            print(f'The man is dead. You had {len(correctGuess)} correct guesses and {len(missedGuess)} wrong guesses. The word is {secretWord}.')
            gameisover = True
    if gameisover:
        if playagain():
            correctGuess = ""
            missedGuess = ""
            secretWord,catagory = randomWord(dataset)
            difficulty = ""
            difficulty = ""
            draw = copy.deepcopy(draw1)
            while difficulty == "":
                difficulty  = input("Choose (H)ard(4),(M)edium(6) or (E)asy:").upper()
                if difficulty  == 'H':
                    del draw[2]
                    del draw[2]
                    del draw[3]
                    del draw[4]
                if difficulty  == "M":
                    del draw[3]
                    del draw[4]
            gameisover = False
        else:
            break





