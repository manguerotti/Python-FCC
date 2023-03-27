class PartyAnimal:
    x=0

    def __init__(self):
        print("Me construí")
    
    def party(self):
        self.x = self.x +1
        print(self.x)

    def __del__(self):
        print("Morí")

an = PartyAnimal()
an.party()
an.party()
an.party()
#an = 42
#print(an)