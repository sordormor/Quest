import random as rand

def Enemy(Difficulty, var):
    if Difficulty == "Easy" and var == 1:
        Weapon = "Пистолетом"
        Damage = 1
        Heal = 2
    elif Difficulty == "Easy" and var == 2:
        Weapon = "Кулаками"
        Damage = 0
        Heal = 2
    elif Difficulty == "Normal" and var == 1:
        Weapon = "Винтовкой"
        Damage = 3
        Heal = 2
    elif Difficulty == "Normal" and var == 2:
        Weapon = "Дробовиком"
        Damage = 3
        Heal = 1
    elif Difficulty == "Hard":
        Weapon = "Огнемётом"
        Damage = 3
        Heal = 1
    return [Weapon , Damage, Heal]

def Enemies(Difficulty):
    Enemies = []
    if Difficulty == "Easy":
        for i in range(rand.randint(0,2)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
                           
    if Difficulty == "Normal":
        for i in range(rand.randint(1,4)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
                           
    if Difficulty == "Hard":
        for i in range(rand.randint(1,3)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
    return Enemies
#class Room():
#    def __init__(self):
#        self.Enemies = Enemies(self.Difficulty)
#        self.NumbEnemies = len(self.Enemies)//3
class EasyRoom():
    Difficulty = "Easy"    
#    Enemies = Enemies("Easy")
#    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class NormalRoom():
    Difficulty = "Normal"
#    Enemies = Enemies(Difficulty)
#    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class HardRoom():
    Difficulty = "Hard"
#    Enemies = Enemies(Difficulty)
#    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class AbillityRoom():
    Difficulty = "Easy"
#    Enemies = Enemies(Difficulty)
    Abillity = rand.randint(1,2)
#    NumbEnemies = len(Enemies)//3
    Win = False
class FinalRoom():
    Difficulty = "Hard"
#    Enemies = [Enemy("Hard",2)]
#    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = True

#a = NormalRoom
#a.__init__(a)
#b = NormalRoom
#b.__init__(b)
#c = NormalRoom
#c.__init__(c)
#print(a.Enemies)
#print(b.Enemies)
#print(c.Enemies)
