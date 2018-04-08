import utilisateur
import map
import robot

def connect(requete,ip_client):
    if requete[1] and len(requete) == 2:
        if requete[1] in utilisateur.utilisateurs_connectes:
            reponse = "450 username Alias already in use. Please try another alias."
        else:
            utilisateur.addUser(requete[1],ip_client)
            reponse = map.getMap()
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
    robot = utilisateur.getUserByIP(ip_client)
    if robot not in robot.paused_robots:
        utilisateur.addRobotToPausedList(robot)
        reponse = "250 Paused"
    else:
        reponse = "444 Already Paused"
    return reponse


def run(ip_client):
    robot = utilisateur.getUserByIP(ip_client)
    if robot in robot.paused_robots:
        utilisateur.delRobotFromPausedList(robot)
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

def exit(ip_client):
    user = utilisateur.getUserByIP(ip_client)
    utilisateur.delUser(user)
    return "100 Déconnexion"
