import random

randomNum = random.randint(1,4)

def chooseASuit(number):
    if number == 1:
        return "Hearts"
    elif number == 2:
        return "Diamonds"
    elif number == 3:
        return "Clubs"
    elif number == 4:
        return "Spades"
    else:
        return "Invalid number"

def chooseAValue(value):
    if value == 1:
        return "Ace"
    elif value == 2:
        return "Two"
    elif value == 3:
        return "Three"
    elif value == 4:
        return "Four"
    elif value == 5:
        return "Five"
    elif value == 6:
        return "Six"
    elif value == 7:
        return "Seven"
    elif value == 8:
        return "Eight"
    elif value == 9:
        return "Nine"
    elif value == 10:
        return "Ten"
    elif value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    else:
        return "Invalid number"
randomValue = random.randint(1,13)

for i in range(10):
    randomNum = random.randint(1,4)
    randomValue = random.randint(1,13)
    print("The card is:", chooseAValue(randomValue), "of", chooseASuit(randomNum))
    print("")