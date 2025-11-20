import Pics as p
import Logs as l
import random as rand
import Classes as clas
p.logo()
p.skip()
if input()=="" or input():
    l.prolog1()
if input()=="" or input():
    l.prolog2() 
if input()=="" or input():
    l.prolog3()
if input()=="" or input():
    l.prolog4()
if input()=="" or input():
    l.prolog5()
if input()=="" or input():
    l.prolog6()
p.skip()
mass = 2

mmass = 5

actives = []

activeabilities = ["Echolocation", "Mindcontrol"]

passives = []

passiveabilities = ["Biosense", "BioMind", "Bioness"]


def room(actives,passives):
    num = rand.randint(1,100)
    if len(actives) == 2 and len(passives) == 3:
        if num >= 50:
            room = clas.FinalRoom
        elif num >= 30:
            room = clas.HardRoom
        elif num >=10:
            room = clas.NormalRoom
        else:
            room = clas.EasyRoom
    elif len(actives) == 2:
        if num >= 50:
            room = clas.FinalRoom
        elif num >= 30:
            room = clas.HardRoom
        elif num >=10:
            room = clas.NormalRoom
        else:
            room = clas.AbillityRoom
    elif len(passives) == 3:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 60:
            room = clas.AbillityRoom
        elif num >= 40:
            room = clas.HardRoom
        elif num >=20:
            room = clas.NormalRoom
        else:
            room = clas.EasyRoom
    elif len(passives) == 2:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 60:
            room = clas.AbillityRoom
        elif num >= 40:
            room = clas.EasyRoom
        elif num >=20:
            room = clas.NormalRoom
        else:
            room = clas.HardRoom
    else:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 70:
            room = clas.AbillityRoom
        elif num >= 20:
            room = clas.EasyRoom
        elif num >=10:
            room = clas.NormalRoom
        else:
            room = clas.HardRoom
    return room
Win = False
Death = False
while Win == False and Death == False:
    rl = room(actives,passives)
    rf = room(actives,passives)
    rr = room(actives,passives)
    l.main(mass)
    flag = False
    while flag == False:
        action = input("Ты можешь направиться <Налево>, <Направо>, <Вперёд> или использовать <Способность>?")
        if action == "Налево":
            p.skip()

            for i in range(rl.NumbEnemies):
                if len(passives)>0:
                    mass -=int(rl.Enemies[1+i*3])-2
                else:
                    mass -=int(rl.Enemies[1+i*3])
                if mass <=0:
                    print("В ожесточённой битве за свою жизнь вы её потеряли")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rl.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rl.Win
            if rl.Abillity == 1 and len(actives)<2:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives}!")
            if rl.Abillity == 2 and len(passives)<3:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False :l.res(rl.Enemies,rl.NumbEnemies)
            flag = True
        elif action == "Направо":
            p.skip()

            for i in range(rr.NumbEnemies):
                if len(passives)>0:
                    mass -=int(rr.Enemies[1+i*3])-2
                else:
                    mass -=int(rr.Enemies[1+i*3])
                if mass <=0:
                    print("В ожесточённой битве за свою жизнь вы её потеряли")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rr.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rr.Win
            if rr.Abillity == 1 and len(actives)<2:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives[-1]}!")
            if rr.Abillity == 2 and len(passives)<3:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False: l.res(rr.Enemies,rr.NumbEnemies)
            flag = True
        elif action == "Вперёд":
            p.skip()

            for i in range(rf.NumbEnemies):
                if len(passives)>0:
                    mass -=int(rf.Enemies[1+i*3])-2
                else:
                    mass -=int(rf.Enemies[1+i*3])
                if mass <=0:
                    print("В ожесточённой битве за свою жизнь вы её потеряли")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rf.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rf.Win
            if rf.Abillity == 1 and len(actives)<2:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives[-1]}!")
            if rf.Abillity == 2 and len(passives)<3:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False: l.res(rf.Enemies,rf.NumbEnemies)
            flag = True
        elif action == "Способность" and len(actives) == 0:
            print("Ты пока не открыл ни каких способностей")
        elif action == "Способность" and len(actives) >= 1:
            print(f"Ты чувствуешь что слева находятся {len(rl.Enemies)/3}, справа {len(rr.Enemies)/3}, впереди {len(rf.Enemies)/3} сущностей.")
        else:
            print("Что-то не то...")
if Win == True:
    print("Или же...")

        
