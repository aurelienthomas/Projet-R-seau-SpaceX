from socket import *
import sys
from datetime import datetime
import time
import utilisateur, map , requetes

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
    sys.exit(1)

TAILLE_TAMPON = 256
sock = socket(AF_INET, SOCK_DGRAM)
#Load map

# Liaison de la socket à toutes les IP possibles de la machine
sock.bind(("", int(sys.argv[1])))
print("Serveur en attente sur le port " + sys.argv[1], file=sys.stderr)
dateInit = datetime.now()
with open("serveurLog.txt", "a") as f:
    f.write(dateInit.strftime("%d/%m/%Y %H:%M:%S") + " Server started\n")
    f.write(dateInit.strftime("%d/%m/%Y %H:%M:%S") + " Listen on: " + sys.argv[1] + "\n")

#Server is listening
while True:
    try:
        # Récupération de la requête du client
        msg = sock.recvfrom(TAILLE_TAMPON)
        # Extraction du message et de l’adresse sur le client
        (mess, adr_client) = msg
        ip_client, port_client = adr_client
        print(f"Requête provenant de {ip_client}. Longueur = {len(mess)}",
                    file=sys.stderr)
        # Construction de la réponse
        request = mess.decode().upper()
        #On écrit la requête reçue
        with open("serveurLog.txt","a") as f:
            date = datetime.now()
            f.write(date.strftime("%d/%m/%Y %H:%M:%S") + f"Received {request} from {adr_client[0]}:{adr_client[1]}\n")


        # Envoi de la réponse au client
        args = request.split(" ")
        if args[0] == "CONNECT":
            reponse = requetes.connect(args,ip_client)
        elif args[0] == "ADD":
            reponse = requetes.add(args,ip_client)
        elif args[0] == "NAME":
            reponse = requetes.name(args, ip_client)
        elif args[0] == "INFO":
            reponse = requetes.info(ip_client)
        elif args[0] == "UP":
            reponse = requetes.up(ip_client)
        elif args[0] == "DOWN":
            reponse = requetes.down(ip_client)
        elif args[0] == "LEFT":
            reponse = requetes.left(ip_client)
        elif args[0] == "RIGHT":
            reponse = requetes.right(ip_client)

        elif args[0] == "ASKTRANSFER":
            reponse = requetes.asktransfer(args,ip_client)
        elif args[0] == "PAUSE":
            reponse = requetes.pause(ip_client)
        elif args[0] == "RUN":
            reponse = requetes.run(ip_client)
        elif args[0] == "QUIT":
            reponse = requetes.quit(ip_client)
            sock.sendto(reponse.encode(), adr_client)
            break
        elif args[0] == "UPDATE":
            reponse = requetes.updateMap()
        else:
            reponse = f"480 Invalid Command"
        sock.sendto(reponse.encode(), adr_client)
        #A ENLEVER POUR LA VERSION FINAL
        #/!\/!\/!\/!\/!\/!\/!\/!\/!\/!\
        modCarte = False
        # /!\/!\/!\/!\/!\/!\/!\/!\/!\
        if modCarte:
            for adrIP in utilisateur.utilisateurs_connectes.values():
                sock.sendto(requetes.updateMap().encode(),(adrIP,port_client))
    except KeyboardInterrupt:
        break

sock.close()
print("Arrêt du serveur", file=sys.stderr)
with open("serveurLog.txt", "a") as f:
    date = datetime.now()
    f.write(date.strftime("%d/%m/%Y %H:%M:%S") + " Server stopped...\n\n")
#Serialization map
map.serializationMap()
map.serializationRessources()
sys.exit(0)
