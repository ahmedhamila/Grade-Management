from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Grade import Note

class Ui_Dialog(object):
    def ajouter(self):
        nInscr=self.comboBoxNumeroInscription.currentText().split(" ")[0]
        code=self.comboBoxCode.currentText().split(" ")[0]
        noteD=self.lineNoteDS.text()
        noteE=self.lineNoteEX.text()
        if(not (noteD.isnumeric() and 20>=float(noteD)>=0)):
            self.showDialog("Invalid Input","Note doit etre numerique entre 0 et 20",True)
            self.lineNoteDS.setText("")
            return
        if(not (noteE.isnumeric() and 20>=float(noteE)>=0)):
            self.showDialog("Invalid Input","Note doit etre numerique entre 0 et 20",True)
            self.lineNoteEX.setText("")
            return
        found=False
        for i in self.ISIMM.Notes:
            if(i.code==code and i.nInscription==nInscr):
                found=True
                break
        if(found):
            self.showDialog("Invalid Input","Note existe deja",True)
            return
        self.showDialog("Success","Ajout Effectué avec succée",False)
        self.ISIMM.ajouterNote(Note(nInscr,code,noteD,noteE))
        self.resetLineEdit()
    
    def resetLineEdit(self):
        self.lineNoteDS.setText("")
        self.lineNoteEX.setText("")

    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def showDialog(self,str,detailed,type):
        msgBox = QMessageBox()
        if(type):
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Information)
        msgBox.setStyleSheet("width: 100px; font-size:15px;")
        msgBox.setText(str)
        msgBox.setDetailedText(detailed)
        msgBox.setWindowTitle("Error Message")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1156, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(450, 40, 221, 35))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 320, 161, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 390, 161, 21))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 250, 161, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(180, 460, 161, 21))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.comboBoxNumeroInscription = QtWidgets.QComboBox(Dialog)
        self.comboBoxNumeroInscription.setGeometry(QtCore.QRect(410, 250, 421, 31))
        self.comboBoxNumeroInscription.setObjectName("comboBoxNumeroInscription")
        self.comboBoxCode = QtWidgets.QComboBox(Dialog)
        self.comboBoxCode.setGeometry(QtCore.QRect(410, 320, 421, 31))
        self.comboBoxCode.setObjectName("comboBoxCode")
        self.lineNoteDS = QtWidgets.QLineEdit(Dialog)
        self.lineNoteDS.setGeometry(QtCore.QRect(410, 390, 421, 30))
        self.lineNoteDS.setObjectName("lineNoteDS")
        self.lineNoteEX = QtWidgets.QLineEdit(Dialog)
        self.lineNoteEX.setGeometry(QtCore.QRect(410, 460, 421, 30))
        self.lineNoteEX.setObjectName("lineNoteEX")
        self.Ajouter = QtWidgets.QPushButton(Dialog)
        self.Ajouter.setGeometry(QtCore.QRect(360, 650, 351, 31))
        self.Ajouter.setObjectName("Ajouter")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1301, 861))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_10.raise_()
        self.label_2.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_11.raise_()
        self.comboBoxNumeroInscription.raise_()
        self.comboBoxCode.raise_()
        self.lineNoteDS.raise_()
        self.lineNoteEX.raise_()
        self.Ajouter.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.comboBoxCode.clear()
        for matiere in self.ISIMM.Matieres:
            self.comboBoxCode.addItem(matiere.code+" "+matiere.designation)
        self.comboBoxNumeroInscription.clear()
        for etudiant in self.ISIMM.Etudiants:
            self.comboBoxNumeroInscription.addItem(etudiant.nInscription+" "+etudiant.nom+" "+etudiant.prenom)
        

        self.Ajouter.clicked.connect(self.ajouter)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Ajouter une note"))
        self.label_2.setText(_translate("Dialog", "Code matière"))
        self.label_8.setText(_translate("Dialog", "Note DS"))
        self.label.setText(_translate("Dialog", "Numéro d\'inscription"))
        self.label_11.setText(_translate("Dialog", "Note EX"))
        self.Ajouter.setText(_translate("Dialog", "Ajouter"))
import Backgrounds
