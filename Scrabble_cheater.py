import sys
import Scrabble as scr
def valid_word(word,rack):
    #Make a copy of rack for every new word so we can Manipulate without changing orginal rack
    available_letters=rack[:]#['a','b','c','d','e','f','g']
    for l in word:#l =dace
        if l not in available_letters:
            return False
        available_letters.remove(l)
    return True
def compute_Score(word):
    #Calculate the scores for the words
    score=0
    for i in word:
        score=score+scr.Scores[i]
    return score

if(len(sys.argv)<2):
    print("Usage: Scrabble_cheater.py [RACK]")
    exit(1)
rack=list(sys.argv[1].lower())#For "Scrabble_cheater.py abcdefg rack =['a','b','c','d','e','f','g']
valid_words=[]

for w in scr.w_List:
    if valid_word(w,rack):
        score=compute_Score(w)
        valid_words.append([score,w])

valid_words.sort()

for play in valid_words:
    score=play[0]
    word=play[1]
    print(word + ": "+str(score))
print("Total word: " + str(len(valid_words)))
