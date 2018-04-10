# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet_reseau.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(503, 514)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.edit_pseudo = QtGui.QLineEdit(Frame)
        self.edit_pseudo.setGeometry(QtCore.QRect(82, 10, 291, 21))
        self.edit_pseudo.setObjectName(_fromUtf8("edit_pseudo"))
        self.label_pseudo = QtGui.QLabel(Frame)
        self.label_pseudo.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.label_pseudo.setObjectName(_fromUtf8("label_pseudo"))
        self.connexion = QtGui.QPushButton(Frame)
        self.connexion.setGeometry(QtCore.QRect(380, 10, 111, 21))
        self.connexion.setObjectName(_fromUtf8("connexion"))
        self.label_carte = QtGui.QLabel(Frame)
        self.label_carte.setGeometry(QtCore.QRect(10, 40, 51, 17))
        self.label_carte.setObjectName(_fromUtf8("label_carte"))
        self.carte = QtGui.QTableWidget(Frame)
        self.carte.setGeometry(QtCore.QRect(10, 60, 481, 321))
        self.carte.setObjectName(_fromUtf8("carte"))
        self.carte.setColumnCount(0)
        self.carte.setRowCount(0)
        self.up = QtGui.QPushButton(Frame)
        self.up.setGeometry(QtCore.QRect(220, 400, 51, 41))
        self.up.setText(_fromUtf8(""))
        self.up.setObjectName(_fromUtf8("up"))
        self.up.setIcon(QIcon("Images/up.png"))
        self.right = QtGui.QPushButton(Frame)
        self.right.setGeometry(QtCore.QRect(280, 430, 51, 41))
        self.right.setText(_fromUtf8(""))
        self.right.setObjectName(_fromUtf8("right"))
        self.up.setIcon(QIcon("Images/right.png"))
        self.left = QtGui.QPushButton(Frame)
        self.left.setGeometry(QtCore.QRect(160, 430, 51, 41))
        self.left.setText(_fromUtf8(""))
        self.left.setObjectName(_fromUtf8("left"))
        self.up.setIcon(QIcon("Images/left.png"))
        self.down = QtGui.QPushButton(Frame)
        self.down.setGeometry(QtCore.QRect(220, 450, 51, 41))
        self.down.setText(_fromUtf8(""))
        self.down.setObjectName(_fromUtf8("down"))
        self.up.setIcon(QIcon("Images/down.png"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Projet_Reseau", None))
        self.label_pseudo.setText(_translate("Frame", "Pseudo :", None))
        self.connexion.setText(_translate("Frame", "Connexion", None))
        self.label_carte.setText(_translate("Frame", "Carte :", None))

