import Pics as p
import Logs as l
import random as rand
import Classes as clas
def room(actives,passives):
    num = rand.randint(1,100)
    if len(actives) == 2 and len(passives) == 3:
        if num >= 50:
            room = clas.FinalRoom
        elif num >= 10:
            room = clas.HardRoom
        else:
            room = clas.NormalRoom
    elif len(actives) == 2:
        if num >= 55:
            room = clas.FinalRoom
        elif num >= 35:
            room = clas.HardRoom
        elif num >=25:
            room = clas.NormalRoom
        else:
            room = clas.AbillityRoom
    elif len(passives) == 3:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 50:
            room = clas.AbillityRoom
        elif num >= 30:
            room = clas.HardRoom
        else:
            room = clas.NormalRoom
    elif len(passives) == 2:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 55:
            room = clas.AbillityRoom
        elif num >= 35:
            room = clas.NormalRoom
        elif num >=15:
            room = clas.HardRoom
        else:
            room = clas.EasyRoom
    elif len(passives) == 1:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 60:
            room = clas.AbillityRoom
        elif num >= 35:
            room = clas.EasyRoom
        elif num >=10:
            room = clas.NormalRoom
        else:
            room = clas.HardRoom
    else:
        if num == 100:
            room = clas.FinalRoom
        elif num >= 60:
            room = clas.AbillityRoom
        elif num >= 20:
            room = clas.EasyRoom
        elif num >=10:
            room = clas.NormalRoom
        else:
            room = clas.HardRoom
    return room
