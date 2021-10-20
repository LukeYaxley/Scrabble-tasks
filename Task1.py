#Code written by Luke Yaxley
with open("scores.txt", "r") as text: #opens scores file as a readable file
    scores = []
    for item in text.readlines():   #reads file and converts it to a 2d list without the \n character
        item = item.strip("\n").split(" ")
        scores.append(item)
    text.close()

with open("dictionary.txt","r") as text: #opens dictionary.txt as readable file
    words = text.readlines()
    dictionary = []
    for item in words:      #splits read items into list format
        item = item.strip("\n")
        dictionary.append(item)
    text.close()


with open("tiles.txt","r") as text: #opens tiles.txt as readable file
    tiles = text.readlines()
    x = []
    for item in tiles:          #splits read items into list format
        item = item.strip("\n")
        x.append(item)
    text.close()
    tiles = x
