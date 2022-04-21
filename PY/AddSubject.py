from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Subject import Matiere


class Ui_Dialog(object):
    def ajouter(self):
        code=self.lineEditCode.text()
        design=self.lineDesignation.text()
        Section=self.comboBoxSection.currentText()
        coeff=self.comboBoxCoefficient.currentText()
        sem=self.comboBoxSemestre.currentText()
        if(not (code.isnumeric() and len(code)>=4)):
            self.showDialog("Invalid Input","Code doit etre numerique de taille minimum 4",True)
            self.lineEditCode.setText("")
            return
        if(not (len(design)>=3)):
            self.showDialog("Invalid Input","Designaion doit etre de taille minimimum 3",True)
            return
        found=False
        for i in self.ISIMM.Matieres:
            if(i.code==code):
                found=True
                break
        if(found):
            self.showDialog("Invalid Input","Code existe deja",True)
            self.lineEditCode.setText("")
            return
        self.showDialog("Success","Ajout Effectué avec succée",False)
        self.ISIMM.ajouterMatiere(Matiere(code,design,Section,coeff,sem))
        self.resetLineEdit()
    
    def resetLineEdit(self):
        self.lineEditCode.setText("")
        self.lineDesignation.setText("")

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
        Dialog.resize(1157, 809)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.Ajouter = QtWidgets.QPushButton(Dialog)
        self.Ajouter.setGeometry(QtCore.QRect(360, 660, 351, 31))
        self.Ajouter.setObjectName("Ajouter")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(410, 200, 421, 30))
        self.lineEditCode.setInputMask("")
        self.lineEditCode.setMaxLength(32767)
        self.lineEditCode.setObjectName("lineEditCode")
        self.comboBoxSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection.setGeometry(QtCore.QRect(410, 341, 421, 31))
        self.comboBoxSection.setObjectName("comboBoxSection")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 270, 161, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(430, 60, 253, 35))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.lineDesignation = QtWidgets.QLineEdit(Dialog)
        self.lineDesignation.setGeometry(QtCore.QRect(410, 270, 421, 30))
        self.lineDesignation.setObjectName("lineDesignation")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 340, 161, 21))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 200, 161, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.comboBoxCoefficient = QtWidgets.QComboBox(Dialog)
        self.comboBoxCoefficient.setGeometry(QtCore.QRect(410, 420, 421, 31))
        self.comboBoxCoefficient.setObjectName("comboBoxCoefficient")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(240, 420, 161, 21))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.comboBoxSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxSemestre.setGeometry(QtCore.QRect(410, 500, 421, 31))
        self.comboBoxSemestre.setObjectName("comboBoxSemestre")
        self.comboBoxSemestre.addItem("")
        self.comboBoxSemestre.addItem("")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(240, 500, 161, 21))
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1261, 861))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.Ajouter.raise_()
        self.lineEditCode.raise_()
        self.comboBoxSection.raise_()
        self.label_2.raise_()
        self.lineDesignation.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.comboBoxCoefficient.raise_()
        self.label_11.raise_()
        self.comboBoxSemestre.raise_()
        self.label_12.raise_()
        self.label_10.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.Ajouter.clicked.connect(self.ajouter)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Ajouter.setText(_translate("Dialog", "Ajouter"))
        self.comboBoxSection.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBoxSection.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.label_2.setText(_translate("Dialog", "Désignation"))
        self.label_10.setText(_translate("Dialog", "Ajouter une matiére"))
        self.label_8.setText(_translate("Dialog", "Section"))
        self.label.setText(_translate("Dialog", "Code"))
        self.comboBoxCoefficient.setItemText(0, _translate("Dialog", "0.5"))
        self.comboBoxCoefficient.setItemText(1, _translate("Dialog", "1"))
        self.comboBoxCoefficient.setItemText(2, _translate("Dialog", "1.5"))
        self.comboBoxCoefficient.setItemText(3, _translate("Dialog", "2"))
        self.label_11.setText(_translate("Dialog", "Coefficient"))
        self.comboBoxSemestre.setItemText(0, _translate("Dialog", "S1"))
        self.comboBoxSemestre.setItemText(1, _translate("Dialog", "S2"))
        self.label_12.setText(_translate("Dialog", "Semestre"))
import Backgrounds
