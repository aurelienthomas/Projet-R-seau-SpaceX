import map


utilisateurs_connectes = {}


def addUser(pseudo,ip):
    utilisateurs_connectes[pseudo] = ip


def delUser(pseudo):
    utilisateurs_connectes.pop(pseudo)


def listOfConnectedUsers():
    list = []
    for userName in utilisateurs_connectes.keys():
        list.append(userName)
    return list


def userIsConnected(ip):
    for user in utilisateurs_connectes.keys():
        if utilisateurs_connectes[user] == ip:
            return True
    return False


def getUserByIP(ip):
    for user in utilisateurs_connectes.keys():
        if utilisateurs_connectes[user] == ip:
            return user


def changeName(newName, robot):
    utilisateurs_connectes[newName] = utilisateurs_connectes.pop(robot["name"])
    robot["name"] = newName
