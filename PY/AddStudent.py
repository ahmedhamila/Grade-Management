from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Student import Etudiant
from PyQt5.QtCore import QDate
class Ui_Dialog(object):
    
    def ajouter(self):
        numInsc=self.lineEditNumeroInscription.text()
        nom=self.lineEditNom.text()
        prenom=self.lineEditPrenom.text()
        date=self.DateNaissance.selectedDate()
        adresse=self.lineEditAdresse.text()
        mail=self.lineEditMail.text()
        telephone=self.lineEditTelephone.text()
        section=self.comboBox.currentText()
        niveau=self.comboBox_2.currentText()
        
        if(not (numInsc.isnumeric() and len(numInsc)>=4)):
            self.showDialog("Invalid Input","Numero d'inscription doit etre numerique de taille minimum 4",True)
            self.lineEditNumeroInscription.setText("")
            return
        if(not (nom.replace(" ","").isalpha())):
            self.showDialog("Invalid Input","Nom doit etre alphabetique",True)
            self.lineEditNom.setText("")
            return
        if(not (prenom.replace(" ","").isalpha())):
            self.showDialog("Invalid Input","Prenom doit etre alphabetique",True)
            self.lineEditPrenom.setText("")
            return
        if(not (date.year()>=2001)):
            self.showDialog("Invalid Input","Année de naissance doit etre au moins 2003",True)
            return
        if(not (adresse.replace(" ","").isalnum() and len(adresse)>=4)):
            self.showDialog("Invalid Input","Adresse doit etre alphanumerique de taille minimimum 4",True)
            return
        if(not (mail.find("@")!=-1 and mail.find(".com")!=-1)):
            self.showDialog("Invalid Input","Mail doit etre de la forme exemple@gmail.com",True)
            return
        if(not (telephone.isnumeric() and len(telephone)==8 and (int(telephone[0]) in {9,5,2}))):
            self.showDialog("Invalid Input","Numero de telephone doit etre de la forme 55436333",True)
            return
        found=False
        for i in self.ISIMM.Etudiants:
            if(i.nInscription==numInsc):
                found=True
                break
        if(found):
            self.showDialog("Invalid Input","Numero d'inscription existe deja",True)
            self.lineEditNumeroInscription.setText("")
            return
        self.showDialog("Success","Ajout Effectué avec succée",False)
        self.ISIMM.ajouterEtudiant(Etudiant(numInsc,nom,prenom,date,adresse,mail,telephone,section,niveau))
        self.resetLineEdit()
    
    def resetLineEdit(self):
        self.lineEditNumeroInscription.setText("")
        self.lineEditNom.setText("")
        self.lineEditPrenom.setText("")
        self.lineEditAdresse.setText("")
        self.lineEditMail.setText("")
        self.lineEditTelephone.setText("")

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
        Dialog.resize(1104, 782)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 100, 161, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEditNumeroInscription = QtWidgets.QLineEdit(Dialog)
        self.lineEditNumeroInscription.setGeometry(QtCore.QRect(430, 100, 421, 30))
        self.lineEditNumeroInscription.setInputMask("")
        self.lineEditNumeroInscription.setMaxLength(32767)
        self.lineEditNumeroInscription.setObjectName("lineEditNumeroInscription")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 150, 161, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEditNom = QtWidgets.QLineEdit(Dialog)
        self.lineEditNom.setGeometry(QtCore.QRect(430, 150, 421, 30))
        self.lineEditNom.setObjectName("lineEditNom")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 200, 161, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEditPrenom = QtWidgets.QLineEdit(Dialog)
        self.lineEditPrenom.setGeometry(QtCore.QRect(430, 200, 421, 30))
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 270, 161, 21))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.DateNaissance = QtWidgets.QCalendarWidget(Dialog)
        self.DateNaissance.setGeometry(QtCore.QRect(430, 240, 421, 211))
        self.DateNaissance.setGridVisible(True)
        self.DateNaissance.setObjectName("DateNaissance")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 480, 161, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.lineEditAdresse = QtWidgets.QLineEdit(Dialog)
        self.lineEditAdresse.setGeometry(QtCore.QRect(430, 480, 421, 30))
        self.lineEditAdresse.setObjectName("lineEditAdresse")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 530, 161, 21))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        
        self.lineEditMail = QtWidgets.QLineEdit(Dialog)
        self.lineEditMail.setGeometry(QtCore.QRect(430, 530, 421, 30))
        self.lineEditMail.setObjectName("lineEditMail")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(260, 580, 161, 21))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lineEditTelephone = QtWidgets.QLineEdit(Dialog)
        self.lineEditTelephone.setGeometry(QtCore.QRect(430, 580, 421, 30))
        self.lineEditTelephone.setObjectName("lineEditTelephone")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(260, 630, 161, 21))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(430, 631, 421, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(260, 680, 161, 21))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 680, 421, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.Ajouter = QtWidgets.QPushButton(Dialog)
        self.Ajouter.setGeometry(QtCore.QRect(380, 740, 351, 31))
        self.Ajouter.setObjectName("Ajouter")
        
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(380, 30, 251, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.DateNaissance.setSelectedDate(QDate(2001,12,26))
        self.Ajouter.clicked.connect(self.ajouter)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Numéro d\'inscription"))
        self.label_2.setText(_translate("Dialog", "Nom"))
        self.label_3.setText(_translate("Dialog", "Prénom"))
        self.label_4.setText(_translate("Dialog", "Date de naissance"))
        self.label_5.setText(_translate("Dialog", "Adresse"))
        self.label_6.setText(_translate("Dialog", "Mail"))
        self.label_7.setText(_translate("Dialog", "Téléphone"))
        self.label_8.setText(_translate("Dialog", "Section"))
        self.label_9.setText(_translate("Dialog", "Niveau d\'étude"))
        self.Ajouter.setText(_translate("Dialog", "Ajouter"))
        self.label_10.setText(_translate("Dialog", "Ajouter un étudiant"))
        self.comboBox.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBox.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBox.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBox.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "3"))
