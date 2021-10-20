#Code written by Luke Yaxley
def getLetterScore(letter): #This function is from task 3
    try:
        scorelist = []
        if len(letter) == 1:
            with open("scores.txt", "r") as scores:
                scorelist = scores.readlines()
                for i in scorelist:
                    if letter.upper() in i:
                        return i[2]
                print("Invalid letter, not found in scores")
        else:
            print("Invalid length, only 1 letter")
    except TypeError:
        print("Invalid input, input should be a string")

def getWordScore(word): # Function takes input of string and calls getletterScore for each letter in turn
    try:
        score = 0
        for i in list(word):
            score += int(getLetterScore(i))
        return score
    except TypeError:
        print("Invalid input, input should be a string")
print(getWordScore("bat"))