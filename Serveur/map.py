import json

def serializationMap():
    with open("map.json","w") as f:
        str = json.dumps(map)
        f.write(str)


def deserializationMap():
    with open("map.json","r") as f:
        data = json.loads(f.read())
    return data


def getMap():
    return str(map)


def getListRessources():
    list = []
    for elem in map["ressources"]:
        list.append(elem["name"])
    return list


def addPosition(pseudo,posStr,cate):
    posStr = posStr.replace("(","")
    posStr = posStr.replace(")","")
    pos = posStr.split(",")
    element={"name": pseudo,
            "x": int(pos[0]),
            "y": int(pos[1])}
    if posAlreadyUsed(element):
        return "430 the coordinate is not free"
    else:
        map[cate].append(element)
        return f"210 {cate} is added"


def posAlreadyUsed(robot):
    for categories in map.keys():
        if categories != "dimensions":
            for elem in map[categories]:
                if elem["x"] == robot["x"] and elem["y"] == robot["y"]:
                    return True
    return False

map = deserializationMap()
