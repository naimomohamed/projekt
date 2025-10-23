class Karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self.hälsa = hälsa
        self.attackkraft = attackkraft


    def attack (self, annan):
        print(f"\n{self.namn} attackerar {annan.namn}!")
        annan.hälsa -= self.attackkraft

        if annan.hälsa <= 0:
            annan.hälsa = 0
            print(f"{annan.namn} förlorar {self.attackkraft} hälsa")
            print(f"{annan.namn} har 0 hälsa kvar och har besegrats.")
        else:
            print(f"{annan.namn} förlorar {self.attackkraft} hälsa.")
            print(f"{annan.namn} har nu {annan.hälsa} hälsa kvar.")

class Mage(Karaktär):
    def attack(self, annan):
        print(f"{self.namn} använder magi!")
        super().attack(annan)   


class Ranger(Karaktär):
    def attack(self, annan):
        print(f"{self.namn} skjuter en pil")
        super().attack(annan)  


class Warrior (Karaktär):
    def attack(self, annan):
        print(f"{self.namn} hugger med svärd!")
        super().attack(annan) 

mage= Mage("Luna", 80, 15)
warrior= Warrior("Elvara", 100, 10)

mage.attack(warrior)
warrior.attack(mage)
mage.attack(warrior)
warrior.attack(mage)