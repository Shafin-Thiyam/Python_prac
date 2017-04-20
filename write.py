file= open("Score.txt","w")
contries=[]
while True:
    participant=input("Participant name:")
    if participant=="Quit":
        print("Quiting...")
        break
    Score=input("Score of " + participant +":")
    file.write(participant+", "+Score+"\n")

file.close()


