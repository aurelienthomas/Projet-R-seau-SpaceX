import json

def serializationMap():
    with open("map.json","w") as f:
        str = json.dumps(map)
        f.write(str)


def deserializationMap():
    with open("map.json","r") as f:
        data = json.loads(f.read())
    return data


def getMapJSON():
    return json.dumps(map)

def getRobot(username):
    for robot in map["robots"]:
        if robot["name"] == username:
            return robot
    return None

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
    if posAlreadyUsed(element["x"],element["y"]):
        return "430 the coordinate is not free"
    else:
        map[cate].append(element)
        return f"210 {cate} is added"


def posAlreadyUsed(x,y):
    for categories in map.keys():
        if categories != "dimensions":
            for elem in map[categories]:
                if elem["x"] == x and elem["y"] == y:
                    return True
    return False

def posCanMove(x,y):
    if x < 0 or x > map["dimensions"][0] or y < 0 or y >  map["dimensions"][1]:
        return False
    for categories in map.keys():
        if categories != "dimensions" and categories != "ressources":
            for elem in map[categories]:
                if elem["x"] == x and elem["y"] == y:
                    return False
    return True

map = deserializationMap()
