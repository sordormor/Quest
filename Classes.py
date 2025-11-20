import random as rand

def Enemy(Difficulty, var):
    if Difficulty == "Easy" and var == 1:
        Weapon = "Pistol"
        Damage = 1
        Heal = 2
    elif Difficulty == "Easy" and var == 2:
        Weapon = "Fists"
        Damage = 0
        Heal = 2
    elif Difficulty == "Normal" and var == 1:
        Weapon = "Rifle"
        Damage = 3
        Heal = 2
    elif Difficulty == "Normal" and var == 2:
        Weapon = "Shotgun"
        Damage = 4
        Heal = 2
    elif Difficulty == "Hard":
        Weapon = "Flamethrower"
        Damage = 3
        Heal = 2
    return [Weapon , Damage, Heal]

def Enemies(Difficulty):
    Enemies = []
    if Difficulty == "Easy":
        for i in range(rand.randint(0,2)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
                           
    if Difficulty == "Normal":
        for i in range(rand.randint(1,2)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
                           
    if Difficulty == "Hard":
        for i in range(rand.randint(1,2)):
            Enemies+=Enemy(Difficulty,rand.randint(1,2))
    return Enemies
            
class EasyRoom():
    Difficulty = "Easy"
    Enemies = Enemies("Easy")
    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class NormalRoom():
    Difficulty = "Normal"
    Enemies = Enemies(Difficulty)
    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class HardRoom():
    Difficulty = "Hard"
    Enemies = Enemies(Difficulty)
    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = False
class AbillityRoom():
    Difficulty = "Easy"
    Enemies = []
    Abillity = rand.randint(1,2)
    NumbEnemies = len(Enemies)//3
    Win = False
class FinalRoom():
    Difficulty = "Easy"
    Enemies = [Enemy("Easy",2)]
    NumbEnemies = len(Enemies)//3
    Abillity = 0
    Win = True

