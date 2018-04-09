import utilisateur
import map
import robot

def connect(requete,ip_client):
    if requete[1] and len(requete) == 2:
        if requete[1] in utilisateur.utilisateurs_connectes:
            reponse = "450 username Alias already in use. Please try another alias."
        else:
            utilisateur.addUser(requete[1],ip_client)
            reponse = map.getMapJSON()
    else:
        reponse = "440 username invalid"
    return reponse


def add(requete,ip_client):
    if utilisateur.userIsConnected(ip_client):
        pseudo = utilisateur.getUserByIP(ip_client)
        reponse = map.addPosition(pseudo,requete[1],"robots")
    else:
        reponse = "User is not connected"
    return reponse


def asktransfer(requete,ip_client):
    reponse = "TO DO"
    return reponse


def pause(ip_client):
    username = utilisateur.getUserByIP(ip_client)
    LPausedRobots = robot.paused_robots
    print(LPausedRobots)
    if username not in LPausedRobots:
        robot.addRobotToPausedList(username)
        reponse = "250 Paused"
    else:
        reponse = "444 Already Paused"
    return reponse


def run(ip_client):
    username = utilisateur.getUserByIP(ip_client)
    LPausedRobots = robot.paused_robots
    print(LPausedRobots)
    if username in LPausedRobots:
        robot.delRobotFromPausedList(username)
        reponse = "260"
    else:
        reponse = "??? Robot is not in pause"
    return reponse


def name(requete, ip_client):
    if requete[1] and len(requete) == 2:
        if requete[1] in utilisateur.utilisateurs_connectes:
            reponse = "450 username Alias already in use. Please try another alias."
        else:
            utilisateur.changeName(requete[1],ip_client)
            reponse = f"200 {requete[1]}"
    else:
        reponse = "440 username invalid"
    return reponse

def info():
    reponse = {}
    listOfUsersOnline = utilisateur.listOfConnectedUsers()
    listOfRessources = map.getListRessources()
    reponse["Ressources"] = listOfRessources
    reponse["Users"] = listOfUsersOnline
    return str(reponse)

def up(ip_client):
    reponse = robot.moveUp(ip_client)
    return reponse


def down(ip_client):
    reponse = robot.moveDown(ip_client)
    return reponse


def left(ip_client):
    reponse = robot.moveLeft(ip_client)
    return reponse


def right(ip_client):
    reponse = robot.moveRight(ip_client)
    return reponse

def updateMap():
    return map.getMapJSON()


def exit(ip_client):
    user = utilisateur.getUserByIP(ip_client)
    if user is not None:
        utilisateur.delUser(user)
    return "100 Déconnexion"
