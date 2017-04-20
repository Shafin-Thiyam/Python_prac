file=open("Score.txt","r")
Scores={}
for i in file:
    entry=i.strip().split(",")
    Scores[entry[0]]=entry[1]

print(Scores)
