import random as r
class Greeter(object):
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("hello "+ self.name)
    def goodbye(self):
        print("Good bye! "+self.name)
class Die(object):
    def __init__(self,sides):
        self.sides=sides
    def roll(self):
        return r.randint(1,self.sides)
class Deck(object):
    def shuffle(self):
        Suits=["Spades","Diamonds","Hearts","Clubs"]
        Ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.Cards=[]
        for suit in Suits:
            for rank in Ranks:
                self.Cards.append(rank+' of '+suit)
        r.shuffle(self.Cards)

    def deal(self):
        return self.Cards.pop()
