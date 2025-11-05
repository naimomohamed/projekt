import random
import time

class Karaktär:
    def __init__(self, namn, hälsa, attackkraft):
        self.namn = namn
        self.hälsa = hälsa
        self.attackkraft = attackkraft
        self.frusen = False


    def attack (self, target):
        print(f"\n{self.namn} attackerar {target.namn}!")
        target.hälsa -= self.attackkraft

        if target.hälsa <= 0:
            target.hälsa = 0
            print(f"{target.namn} förlorar {self.attackkraft} hälsa")
            print(f"{target.namn} har 0 hälsa kvar och har besegrats.")
        else:
            print(f"{target.namn} förlorar {self.attackkraft} hälsa.")
            print(f"{target.namn} har nu {target.hälsa} hälsa kvar.")

    def special_attack (self, target):
        pass



class Mage(Karaktär):
    def attack(self, target):
        print(f"{self.namn} använder magi!")
        super().attack(target)   

    def special_attack(self, target):
        if self.mana >= 20:
            print(f"{self.namn} använder *eldstorm*")
            skada = self.attackkraft * 2
            target.hälsa -= skada
            self.mana -= 20 
            print(f"{target.namn} tar {skada} skada. ({self.mana} mana kvar)")
        else:
            print(f"{self.namn} har inte tillräckligt med mana för att använda eldstorm!")


class Ranger(Karaktär):
    def attack(self, target):
        print(f"{self.namn} skjuter en pil")
        super().attack(target)  
    def special_attack(self, target):
        if self.mana >= 15:
            print(f"{self.namn} använder *isstrom*")
            skada = self.attackkraft + 10
            target.hälsa -= skada
            self.mana -= 15
            target.frusen = True
            print(f"{target.namn} tar {skada} skada. ({self.mana} mana kvar!)")
        else:
            print(f"{self.namn} är för trött för att använda isstorm!")

class Warrior (Karaktär):
    def attack(self, target):
        print(f"{self.namn} hugger med svärd!")
        super().attack(target) 

    def special_attack(self, target):
        if self.mana >= 10:
            print(f"{self.namn} använder *dubbelpil*.")
            skada = int(self.attackkraft * 1.5)
            target.hälsa -= skada
            self.mana -= 10
            print(f"{target.namn} tar {skada} skada. ({self.mana} fokus kvar)")
        else:
            print(f"{self.namn} har inte nog fokus för att använda dubbelpil!")



class Arena:
    def __init__(self, karaktärer):
        self.karaktärer = karaktärer

    def välj_kämpar(self):
        return random.sample(self.karaktärer, 2)

    def strid(self):
        k1, k2 = self.välj_kämpar()
        print(f"striden börjar mellan {k1.namn} och {k2.namn}!\n")
        runda = 1
        while k1.hälsa > 0 and k2.hälsa > 0:
            print(f"-----Runda{runda}-----")
            time.sleep(0.8)    
            if k1.frusen:
                print(f"{k1.namn} är frusen och kan inte attackera denna rundan")
                k1.frusen = False
            else:
                if random.random() < 0.3:
                    k1.special_attack(k2)
                else:
                    k1.attack(k2)
            if k2.hälsa <= 0:
                print(f"\n {k2.namn} är besegrad! {k1.namn} vinner!")

            if k2.frusen:
                print(f"{k2.namn} är frusen och kan inte spela det här runda!")
                k2.frusen = False
            else:
                if random.random() <= 0.3:
                    k2.special_attack(k1)
                else:
                    k2.attack(k1)

            if k1.hälsa <= 0:
                print(f"\n {k1.namn} besegrad! {k2.namn} vinner!")
                break

            runda += 1
            time.sleep(1)

mage= Mage("Luna", 80, 15, 40)
warrior= Warrior("Elvara", 100, 10, 30)
ranger = Ranger("Sylvia", 90, 12, 25)

arena = Arena([mage, warrior, ranger])
arena.strid()