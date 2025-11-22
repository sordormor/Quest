import Pics as p
import Logs as l
import random as rand
import Classes as clas
import Gen as g
p.logo()
p.skip(3)
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
p.skip(3)
mass = 2

mmass = 5

actives = []

activeabilities = ["Эхолокация (Позволяет определять сколько существ впереди)", "Порабощение (Позволяет управлять другими существами)"]

passives = []

passiveabilities = ["Био-Чутьё (Позволяет заранее чувствовать опасность, что снижает получаемые повреждения в сражении с некоторыми врагами)", "БиоСплит (Позволяет добраться до более защищённых комнат)", "Биогинесс (Позволяет добраться до более защищённых комнат)"]


Win = False
Death = False
while Win == False and Death == False:
    rl = g.room(actives,passives)
    if rl.Abillity !=0:
        rl.Abillity = rand.randint(1,2)
    rl.Enemies = clas.Enemies(rl.Difficulty)
    rl.NumbEnemies = len(rl.Enemies)//3
    rf = g.room(actives,passives)
    if rf.Abillity !=0:
        rf.Abillity = rand.randint(1,2)
    rf.Enemies = clas.Enemies(rf.Difficulty)
    rf.NumbEnemies = len(rf.Enemies)//3
    rr = g.room(actives,passives)
    if rr.Abillity !=0:
        rr.Abillity = rand.randint(1,2)
    rr.Enemies = clas.Enemies(rr.Difficulty)
    rr.NumbEnemies = len(rr.Enemies)//3
    l.main(mass)
    p.skip(1)
    flag = False
    while flag == False:
        action = input("Ты можешь направиться <Налево>, <Направо>, <Вперёд> или использовать <Способность>?\n")


        if action == "Налево":
            p.skip(2)
            for i in range(rl.NumbEnemies):
                if rl.Enemies[0+i*3] != "Огнемёт" and len(passives) > 0:
                    mass -= int(rl.Enemies[1+i*3]) - 2
                elif rl.Enemies[0+i*3] == "Огнемёт" and len(actives) == 2:
                    mass -= int(rl.Enemies[1+i*3]) - 2
                else:
                    mass -= int(rl.Enemies[1+i*3])
                if mass <=0:
                    p.Dscreen()
                    print(f"В ожесточённой битве с врагом, вооружённым {rl.Enemies[0]}, вы потеряли свою жизнь...")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rl.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rl.Win
            if rl.Abillity == 1 and len(actives)<2 and Death == False:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives[-1]}!")
            if rl.Abillity == 2 and len(passives)<3 and Death == False:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False :l.res(rl.Enemies,rl.NumbEnemies)
            flag = True

            
        elif action == "Направо":
            p.skip(2)

            for i in range(rr.NumbEnemies):
                if rr.Enemies[0+i*3] != "Огнемёт" and len(passives) > 0:
                    mass -= int(rr.Enemies[1+i*3]) - 2
                elif rr.Enemies[0+i*3] == "Огнемёт" and len(actives) == 2:
                    mass -= int(rr.Enemies[1+i*3]) - 2
                else:
                    mass -= int(rr.Enemies[1+i*3])
                if mass <=0:
                    p.Dscreen()
                    print(f"В ожесточённой битве с врагом, вооружённым {rr.Enemies[0]}, вы потеряли свою жизнь...")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rr.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rr.Win
            if rr.Abillity == 1 and len(actives)<2 and Death == False:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives[-1]}!")
            if rr.Abillity == 2 and len(passives)<3 and Death == False:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False: l.res(rr.Enemies,rr.NumbEnemies)
            flag = True

            
        elif action == "Вперёд":
            p.skip(2)
            for i in range(rf.NumbEnemies):
                if rf.Enemies[0+i*3] != "Огнемёт" and len(passives) > 0:
                    mass -= int(rf.Enemies[1+i*3]) - 2
                elif rf.Enemies[0+i*3] == "Огнемёт" and len(actives) == 2:
                    mass -= int(rf.Enemies[1+i*3]) - 2
                else:
                    mass -= int(rf.Enemies[1+i*3])
                if mass <=0:
                    p.Dscreen()
                    print(f"В ожесточённой битве с врагом, вооружённым {rf.Enemies[0]}, вы потеряли свою жизнь...")
                    print(f"Вы смогли открыть {actives}, {passives}")
                    print("Удачи в следующий раз!")
                    Death = True
                    break
                mass += int(rf.Enemies[2+i*3])
            if mass > mmass:
                mass = mmass
            Win = rf.Win
            if rf.Abillity == 1 and len(actives)<2 and Death == False:
                actives.append(activeabilities[len(actives)])
                print(f"Вы открыли {actives[-1]}!")
            if rf.Abillity == 2 and len(passives)<3 and Death == False:
                passives.append(passiveabilities[len(passives)])
                print(f"Вы открыли {passives[-1]}!")
            if Death == False: l.res(rf.Enemies,rf.NumbEnemies)
            flag = True
        elif action == "Способность" and len(actives) == 0:
            print("Ты пока не открыл ни каких способностей")
        elif action == "Способность" and len(actives) >= 1:
            print(f"Ты чувствуешь что слева находятся {len(rl.Enemies)//3}, справа {len(rr.Enemies)//3}, впереди {len(rf.Enemies)//3} сущностей.")
        else:
            print("Что-то не то...")
    p.fight(rand.randint(1,15))
if Win == True:
    print("Или же...")
    p.skip(3)
    if input()=="" or input():
        l.End1()
    if input()=="" or input():
        l.End2()
        p.End()
while True:
    if input("Чтобы закрыть окно введите <выход>") == "выход":
        break
