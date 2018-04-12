from PyQt4 import QtGui, QtCore
from fen_principale import Ui_Form
from socket import *
import sys
import json

class MajQt(QtGui.QWidget, Ui_Form):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
	
	def charger_map(self, mapjson):
		self.map = json.loads(mapjson)
		self.carte.setColumnCount(self.map["dimensions"][0])
		self.carte.setRowCount(self.map["dimensions"][1])
		for x in range(self.map["dimensions"][0]):
			self.carte.setColumnWidth(x, 50)
		for y in range(self.map["dimensions"][1]):
			self.carte.setRowHeight(y, 30)
		self.carte.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		elements_bloquants = self.map["blockingElements"]
		for element in elements_bloquants:
			self.carte.setItem(element["y"],element["x"],QtGui.QTableWidgetItem(element["name"]))
		ressources = self.map["ressources"]
		for ressource in ressources:
			self.carte.setItem(ressource["y"],ressource["x"],QtGui.QTableWidgetItem(ressource["name"]))
		robots = self.map["robots"]
		for robot in robots:
			self.carte.setItem(robot["y"],robot["x"],QtGui.QTableWidgetItem(robot["name"]))
	
	def charger_info(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "INFO"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			print(reponse.decode())
			if "200" == reponse.decode().split(" ")[0]:
				infojson = reponse.decode().split(" ",1)[1]
				info = json.loads(infojson)
				self.text_ressources.setText(', '.join(info["Ressources"]))
				self.text_joueurs.setText(', '.join(info["Users"]))
	
	@QtCore.pyqtSlot()
	def on_connexion_clicked(self):
		self.msg_serv.setText(self.edit_pseudo.text())
		if len(sys.argv) != 3:
			print("Usage: "+sys.argv[0]+" <ip> <port>", file=sys.stderr)
			sys.exit(1)
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "CONNECT "+self.edit_pseudo.text()
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "440" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Le pseudo que vous avez choisi n'est pas valide.")
				self.edit_pseudo.setText("")
			elif "450" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Le pseudo que vous avez choisi est déjà utilisé.")
				self.edit_pseudo.setText("")
			else:
				self.msg_serv.setText("Connexion réussie !")
				self.pseudo.setText(self.edit_pseudo.text())
				self.edit_pseudo.setText("")
				mapjson = reponse.decode().split(" ",1)[1]
				print(mapjson)
				self.charger_map(mapjson)
				self.charger_info()

	@QtCore.pyqtSlot()
	def on_changer_pseudo_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "NAME "+self.edit_pseudo.text()
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "200" == reponse.decode().split(" ")[0]:
				self.pseudo.setText(self.edit_pseudo.text())
				self.msg_serv.setText("Pseudo changé.")
				self.edit_pseudo.setText("")
				self.charger_info()
			if "480" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Impossible de changer le pseudo.")
				self.edit_pseudo.setText("")
	
	@QtCore.pyqtSlot()
	def on_ajouter_robot_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "ADD ("+str(int(self.edit_x.text())-1)+","+str(int(self.edit_y.text())-1)+")"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "210" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Robot ajouté !")
				self.edit_x.setText("")
				self.edit_y.setText("")
			if "430" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Impossible d'ajouter le robot aux coordonnées indiquées.")
				self.edit_x.setText("")
				self.edit_y.setText("")

	@QtCore.pyqtSlot()
	def on_up_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "DOWN"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "270" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement vers le haut effectué.")
			if "480" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement impossible.")
	
	@QtCore.pyqtSlot()
	def on_right_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "RIGHT"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "270" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement vers la droite effectué.")
			if "480" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement impossible.")
	
	@QtCore.pyqtSlot()
	def on_down_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "UP"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "270" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement vers le bas effectué.")
			if "480" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement impossible.")
	
	@QtCore.pyqtSlot()
	def on_left_clicked(self):
		with socket(AF_INET, SOCK_DGRAM) as sock:
			commande = "LEFT"
			sock.sendto(commande.encode(), (sys.argv[1], int(sys.argv[2])))
			reponse, _ = sock.recvfrom(1028)
			sock.close()
			if "270" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement vers la gauche effectué.")
			if "480" == reponse.decode().split(" ")[0]:
				self.msg_serv.setText("Déplacement impossible.")
	"""	
	@QtCore.pyqtSlot()
	def on_transfert_clicked(self):
		#code pour le transfert
	
	@QtCore.pyqtSlot()
	def on_pause_clicked(self):
		#code pour mettre en pause
	
	@QtCore.pyqtSlot()
	def on_run_clicked(self):
		#code pour relancer"""

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	win = MajQt()
	win.show()
	sys.exit(app.exec_())