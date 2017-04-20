import Scrabble as scr
#file =open("sowpods.txt","r")
#w_List=[]
letters="abcdefghijklmnopqrstuvwxyz"

#for i in file:
#    w_List.append(i.lower().strip())

#file.close()
#for word in w_List:
#    if "q" in word and "u" not in word :
#        print(word)



def Has_Double(l):
  for w in scr.w_List:
      if l+l in w:
          return True
  return False

def Has_All_Vowels(w):
       if 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w:
          return True
       return False

for l in letters:
    if not Has_Double(l):
        print(l +" never appeared double")

counter=0

for w in scr.w_List:
    if Has_All_Vowels(w):
        print(w)
        counter=counter+1
print("Total words with all vowels in it is "+str(counter))

