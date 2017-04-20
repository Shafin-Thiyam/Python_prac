def Starts_With_vowel(Name_list):
    Vowel=[]
    for i in Name_list:
        if i[0] in 'AEIOU':
            Vowel.append(i)
    return Vowel

Name=["Shafin","Amina","Haiqa"]
print(Starts_With_vowel(Name))

