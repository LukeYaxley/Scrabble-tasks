#Code written by Luke Yaxley
def anagramPossible(word,myTiles): #Function takes input of possible word and list of tiles and then outputs whether the word given is a possible anagram
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
        return None
print(anagramPossible("SWET",["T","Y","S","E","U","W","I"]))