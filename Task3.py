#Code written by Luke Yaxley
def getLetterScore(letter):     #Function takes in string and outputs the score of the letter unless user inputs non string or invalid length string. Also if the letter isn't in the text file
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


print(getLetterScore("d"))
