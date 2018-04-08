from socket import *
import sys
import json
# 8007
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
    sys.exit(1)

TAILLE_TAMPON = 1028
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
print(SERVER,PORT)

with socket(AF_INET, SOCK_DGRAM) as sock:
    """
    while True:
        cmd = input("Entrez votre commande: ")
        if cmd == "quit":
            break
    """
    sock.sendto("connect Oa".encode(), (SERVER, PORT))
    reponse, _ = sock.recvfrom(TAILLE_TAMPON)
    print(reponse.decode())

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.sendto("add (1,2)".encode(), (SERVER, PORT))
    reponse, _ = sock.recvfrom(TAILLE_TAMPON)
    print(reponse.decode())


with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.sendto("info".encode(), (SERVER, PORT))
    reponse, _ = sock.recvfrom(TAILLE_TAMPON)
    print(reponse.decode())



with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.sendto("EXIT".encode(), (SERVER, PORT))
    reponse, _ = sock.recvfrom(TAILLE_TAMPON)
    print(reponse.decode())
