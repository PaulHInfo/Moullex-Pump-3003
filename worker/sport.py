from worker import fileReader
import random
# type = 1 -> endurance, type = 2 -> explosif
def creatExos(part, nbExo,type):
    if nbExo <= 0:
        nbExo = random.randint(3, 6)
    listExo = fileReader.getData(part)
    #for exo in listExo:
        #print(exo["name"])
    # 1 ) Choisir x exo au hasard (x = nbExo)
    listExoSelectionne = []
    i = 0
    while 1 :
        e = listExo[random.randint(0, len(listExo)-1)]
        # check si e = i-1
        if len(listExoSelectionne) != 0:
            if listExoSelectionne[i-1]["name"] == e["name"]:
                #print("same name")
                continue
        listExoSelectionne.append(e)
        i = i + 1
        if i == nbExo:
            break
    # 2 ) def si explo ou endu
    for e in listExoSelectionne:
        #print(e["name"])
        if type%2==0:
            #si explo
            e["series"] = random.randint(3, 6)
            e["rep"] = random.randint(8, 12)
            e["consigne"] = "Donne un max d'explosivité"
        else :
            #si endu
            e["series"] = random.randint(7, 10)
            e["rep"] = random.randint(12, 20)
            e["consigne"] = "tien le plus longtemps possible, si tu peux encore va jusqu'à l'echec"
    #print(listExoSelectionne)
    return listExoSelectionne


def creatMsg(listExo, part):
    msg ='''Salut jeune sportif ! \ntu as voulu une grosse séance '''
    msg = msg  + part + '''. La voici ! tu vas devoir fair ''' + str(len(listExo)) + ''' exerices ! \nLETSSSGOOO !\n\n'''
    for e in listExo:
        txt = e["name"] +"\t"+ str(e["series"])+"x"+ str(e["rep"]) + "\n"
        msg = msg + txt
    print(msg)
    return msg

async def chekCommande(cmd: str):
    print("cmd")
    print(cmd)
    parts = cmd.split()
    parsed = {"command": parts[0]}
    for part in parts[1:]:
        if part.startswith("--"):
            key = part[2:]
            parsed[key] = None
        elif key:
            parsed[key] = part
            key = None
    # --type == en && ex
    type = 1
    part = ""
    print(parsed)
    if 'type' in parsed:
        print(parsed["type"])
        if parsed["type"] != "en" and parsed["type"] != "ex":
            if parsed["type"] == "en":
                type = 1
            else:
                type = 2
        else:
            print("value null")
            return "ERROR PARA"
    else:
        print("value null")
    if "part" in parsed:
        match parsed["part"]:
            case "bras":
                part = parsed["part"]
            case "pecs":
                part = parsed["part"]
            case "jambe":
                part = parsed["part"]
            case _:
                return "ERROR PARA"
    return creatMsg(creatExos(part, 6, parts), part)
