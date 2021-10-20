#Code written by Luke Yaxley
def onlyEnglishLetters(word): #Task 2
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    try:
        for i in word:
            if i.lower() not in alphabet:
                return False
        return True
    except TypeError:
        print("Error, input needs to be string")
        return False


def wordInDictionary (word,dictionary):# Takes in string and dictionary in list form and then checks whether word is in the list
    if word.upper() in dictionary:
        return True
    else:
        return False


def isValid(word, myTiles, dictionary):# Function that checks to make sure all other conditional functions return true
    if onlyEnglishLetters(word) == False:
        return False
    elif wordInDictionary(word, dictionary) == False:
        return False
    elif anagramPossible(word, myTiles) == False:
        return False
    else:
        return True


def testScript():#Script to check the program works
    with open("dictionary.txt", "r") as text:
        words = text.readlines()
        dictionary = []
        for item in words:
            item = item.strip("\n")
            dictionary.append(item)
        text.close()
    print(isValid("Bat",["T","Y","S","E","U","W","I"], dictionary))


def anagramPossible(word,myTiles): #Task5
    try:
        if len(myTiles) == 7:
            wordList =[]
            matchedLetters = []
            for i in range(len(word)):
                wordList.append(word[i])
            for j in wordList:
                for k in range(len(myTiles)):
                    if j == myTiles[k]:
                        if k not in matchedLetters:
                            matchedLetters.append(k)
                        else:
                            continue
            if len(wordList) == len(matchedLetters):
                return True
            else:
                return False
        else:
            print("Invalid amount of tiles, only 7 tiles allowed")
            return None
    except TypeError:
        print("Invalid input type")
        return None #


testScript()
