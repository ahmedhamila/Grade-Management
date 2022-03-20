from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
class Ui_Dialog(object):
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
        

    def comboChanged(self):
        nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
        if(self.ISIMM.getEtudiant(nInscr)!=False):
            self.lineEditAdresse.setText(self.ISIMM.getEtudiant(nInscr).adresse)
            self.lineEditMail.setText(self.ISIMM.getEtudiant(nInscr).mail)
            self.lineEditTelephone.setText(self.ISIMM.getEtudiant(nInscr).telephone)
    def modifier(self):
        adr=self.lineEditAdresse.text()
        mai=self.lineEditMail.text()
        tel=self.lineEditTelephone.text()
        if(not (adr.replace(" ","").isalnum() and len(adr)>=4)):
            self.showDialog("Invalid Input","Adresse doit etre alphanumerique de taille minimimum 4",True)
            return
        if(not (mai.find("@")!=-1 and mai.find(".com")!=-1)):
            self.showDialog("Invalid Input","Mail doit etre de la forme exemple@gmail.com",True)
            return
        if(not (tel.isnumeric() and len(tel)==8 and (int(tel[0]) in {9,5,2}))):
            self.showDialog("Invalid Input","Numero de telephone doit etre de la forme 55436333",True)
            return
        self.showDialog("Success","Modification Effectué avec succée",False)
        nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
        self.ISIMM.getEtudiant(nInscr).adresse=adr
        self.ISIMM.getEtudiant(nInscr).mail=mai
        self.ISIMM.getEtudiant(nInscr).telephone=tel

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
        Dialog.resize(1103, 783)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(390, 40, 291, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.comboBoxEtudiant = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiant.setGeometry(QtCore.QRect(450, 200, 421, 31))
        self.comboBoxEtudiant.setObjectName("comboBoxEtudiant")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 190, 171, 41))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 510, 161, 21))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lineEditMail = QtWidgets.QLineEdit(Dialog)
        self.lineEditMail.setGeometry(QtCore.QRect(450, 460, 421, 30))
        self.lineEditMail.setObjectName("lineEditMail")
        self.lineEditAdresse = QtWidgets.QLineEdit(Dialog)
        self.lineEditAdresse.setGeometry(QtCore.QRect(450, 410, 421, 30))
        self.lineEditAdresse.setObjectName("lineEditAdresse")
        self.lineEditTelephone = QtWidgets.QLineEdit(Dialog)
        self.lineEditTelephone.setGeometry(QtCore.QRect(450, 510, 421, 30))
        self.lineEditTelephone.setObjectName("lineEditTelephone")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 460, 161, 21))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 410, 161, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.Modifier = QtWidgets.QPushButton(Dialog)
        self.Modifier.setGeometry(QtCore.QRect(390, 700, 351, 31))
        self.Modifier.setObjectName("Modifier")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        for etudiant in self.ISIMM.Etudiants:
            self.comboBoxEtudiant.addItem(etudiant.nInscription+" "+etudiant.nom+" "+etudiant.prenom)
        self.comboChanged()    
        self.comboBoxEtudiant.currentTextChanged.connect(self.comboChanged)
        self.Modifier.clicked.connect(self.modifier)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Modifier un étudiant"))
        self.label.setText(_translate("Dialog", "Selectionner un étudiant"))
        self.label_7.setText(_translate("Dialog", "Téléphone"))
        self.label_6.setText(_translate("Dialog", "Mail"))
        self.label_5.setText(_translate("Dialog", "Adresse"))
        self.Modifier.setText(_translate("Dialog", "Modifier"))
