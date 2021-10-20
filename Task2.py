#Code written by Luke Yaxley
def onlyEnglishLetters(word): #Function takes in a word in the form of a string and outputs true or false depending on whether each letter is in the list alphabet
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    try:
        for i in word:
            if i.lower() not in alphabet:
                return False
        return True
    except TypeError:
        print("Error, input not valid")
        return False  #This is outputted when the function is run with a datatype other than string
