def vowel(val):
    return val[0] in 'AEIOU'

Name=input("Enter your name: ")
if(vowel(Name)):
    print(Name+" starts with vowels")
else:
    print(Name+" not starts with vowels")

