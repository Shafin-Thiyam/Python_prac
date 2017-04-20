import sys
import random
if len(sys.argv)< 2:
    print("please supply flash card files.")
    exit(1)
print(sys.argv[0])
f_c=sys.argv[1]
f=open(f_c,"r")
QnA={}

for i in f:
    QA=i.strip().split(':')
    QnA[QA[0]]=QA[1]
f.close()

print("Welcome to Sabse Bada Foodie")
print("Press Q to quit")
print("")
States=list(QnA.keys())
while True:
    state=random.choice(States)
    Delicacy=QnA[state]
    Ans=str(input("Whats popular dish of "+state +"?")).lower()
    if Ans =='q':
        print("Thanks for participating Good bye!")
        break
    elif str(Ans).lower()==str(Delicacy).lower():
        print("You are Correct foody")
    else:
        print("Wrong answer, popular food of "+state+" is " + Delicacy)




