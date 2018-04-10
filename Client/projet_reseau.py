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
			self.carte.setItem(element["x"]+1,element["y"]+1,QtGui.QTableWidgetItem(element["name"]))
		ressources = self.map["ressources"]
		for ressource in ressources:
			self.carte.setItem(ressource["x"]+1,ressource["y"]+1,QtGui.QTableWidgetItem(ressource["name"]))
		robots = self.map["robots"]
		for robot in robots:
			self.carte.setItem(robot["x"]+1,robot["y"]+1,QtGui.QTableWidgetItem(robot["name"]))
	
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

	@QtCore.pyqtSlot()
	def on_changer_pseudo_clicked(self):
		#ajout necessaire
		self.pseudo.setText(self.edit_pseudo.text())
		self.edit_pseudo.setText("")
	
	"""@QtCore.pyqtSlot()
	def on_up_clicked(self):
		#code pour deplacer le robot de une case vers le haut
	
	@QtCore.pyqtSlot()
	def on_right_clicked(self):
		#code pour deplacer le robot de une case vers la droite
	
	@QtCore.pyqtSlot()
	def on_down_clicked(self):
		#code pour deplacer le robot de une case vers le bas
	
	@QtCore.pyqtSlot()
	def on_left_clicked(self):
		#code pour deplacer le robot de une case vers la gauche
	
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