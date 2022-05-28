# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
print ("Welcome to the anagram Detector \n Enter your the words and if they are anagrams, you will get a response: True. \n If they are not anagrams, you will get a response: False. ")

w1 = input("Enter your first word here: ")
w2 = input("Enter your second word here: ")

def find_anagram(w1, w2):    
    if (sorted (w1)== sorted (w2)):
        return True
    else:
        return False
print(find_anagram(w1, w2))
