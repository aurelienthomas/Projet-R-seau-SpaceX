# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projet_reseau.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(506, 514)
        self.up = QtGui.QPushButton(Form)
        self.up.setGeometry(QtCore.QRect(210, 400, 51, 41))
        self.up.setText(_fromUtf8(""))
        self.up.setObjectName(_fromUtf8("up"))
        self.down = QtGui.QPushButton(Form)
        self.down.setGeometry(QtCore.QRect(210, 450, 51, 41))
        self.down.setText(_fromUtf8(""))
        self.down.setObjectName(_fromUtf8("down"))
        self.left = QtGui.QPushButton(Form)
        self.left.setGeometry(QtCore.QRect(150, 430, 51, 41))
        self.left.setText(_fromUtf8(""))
        self.left.setObjectName(_fromUtf8("left"))
        self.right = QtGui.QPushButton(Form)
        self.right.setGeometry(QtCore.QRect(270, 430, 51, 41))
        self.right.setText(_fromUtf8(""))
        self.right.setObjectName(_fromUtf8("right"))
        self.carte = QtGui.QTableWidget(Form)
        self.carte.setGeometry(QtCore.QRect(10, 60, 481, 321))
        self.carte.setObjectName(_fromUtf8("carte"))
        self.carte.setColumnCount(0)
        self.carte.setRowCount(0)
        self.label_carte = QtGui.QLabel(Form)
        self.label_carte.setGeometry(QtCore.QRect(10, 40, 51, 17))
        self.label_carte.setObjectName(_fromUtf8("label_carte"))
        self.label_pseudo = QtGui.QLabel(Form)
        self.label_pseudo.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.label_pseudo.setObjectName(_fromUtf8("label_pseudo"))
        self.connexion = QtGui.QPushButton(Form)
        self.connexion.setGeometry(QtCore.QRect(380, 10, 111, 21))
        self.connexion.setObjectName(_fromUtf8("connexion"))
        self.edit_pseudo = QtGui.QLineEdit(Form)
        self.edit_pseudo.setGeometry(QtCore.QRect(82, 10, 291, 21))
        self.edit_pseudo.setObjectName(_fromUtf8("edit_pseudo"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Projet_Reseau", None))
        self.label_carte.setText(_translate("Form", "Carte :", None))
        self.label_pseudo.setText(_translate("Form", "Pseudo :", None))
        self.connexion.setText(_translate("Form", "Connexion", None))

