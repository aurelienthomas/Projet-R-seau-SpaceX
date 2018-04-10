from PyQt4 import QtGui
from fen_principale import Ui_Frame

class MajQt(QtGui.QFrame, Ui_Frame):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	win = MajQt()
	win.show
	sys.exit(app.exec_())