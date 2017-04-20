file= open("Contries.txt","r")
contries=[]
for l in file:
    l=l.strip()
    #print(l)
    contries.append(l)
file.close()
print("Following Contries whose name starts with vowels")
for i in contries:
    if i[0]in 'AEIOU':
        print(i)

