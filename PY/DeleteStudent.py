from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(object):
    def deleteEtudiant(self):
        if(self.SupprimerEtudiant.isChecked()):
            nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
            if(self.ISIMM.getEtudiant(nInscr)!=False):
                self.ISIMM.Etudiants.remove(self.ISIMM.getEtudiant(nInscr))
            self.comboBoxEtudiant.clear()
            for i in self.ISIMM.Etudiants:
                self.comboBoxEtudiant.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        if(self.SupprimerEtudiantSection.isChecked()):
            nInscr=self.comboBoxEtudiantSection.currentText().split(" ")[0]
            if(self.ISIMM.getEtudiant(nInscr)!=False):
                self.ISIMM.Etudiants.remove(self.ISIMM.getEtudiant(nInscr))
            self.comboBoxEtudiantSection.clear()
            for i in self.ISIMM.Etudiants:
                if(i.section==self.comboBoxSection1.currentText()):
                    self.comboBoxEtudiantSection.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        if(self.SupprimerEtudiantNiveau.isChecked()):
            nInscr=self.comboBoxEtudiantNiveau.currentText().split(" ")[0]
            if(self.ISIMM.getEtudiant(nInscr)!=False):
                self.ISIMM.Etudiants.remove(self.ISIMM.getEtudiant(nInscr))
            self.comboBoxEtudiantNiveau.clear()
            for i in self.ISIMM.Etudiants:
                if(i.niveauEtude==self.comboBoxNiveau1.currentText()):
                    self.comboBoxEtudiantNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        if(self.SupprimerEtudiantSectionNiveau.isChecked()):
            nInscr=self.comboBoxEtudiantSectionNiveau.currentText().split(" ")[0]
            if(self.ISIMM.getEtudiant(nInscr)!=False):
                self.ISIMM.Etudiants.remove(self.ISIMM.getEtudiant(nInscr))
            self.comboBoxEtudiantSectionNiveau.clear()
            for i in self.ISIMM.Etudiants:
                if(i.niveauEtude==self.comboBoxNiveau2.currentText() and i.section==self.comboBoxSection2.currentText()):
                    self.comboBoxEtudiantSectionNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)

            
    def comboSectionChanged(self):
        self.comboBoxEtudiantSection.clear()
        for i in self.ISIMM.Etudiants:
            if(i.section==self.comboBoxSection1.currentText()):
                self.comboBoxEtudiantSection.addItem(i.nInscription+" "+i.nom+" "+i.prenom)

    def comboNiveauChanged(self):
        self.comboBoxEtudiantNiveau.clear()
        for i in self.ISIMM.Etudiants:
            if(i.niveauEtude==self.comboBoxNiveau1.currentText()):
                self.comboBoxEtudiantNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
    def comboSectionNiveauChanged(self):
        self.comboBoxEtudiantSectionNiveau.clear()
        for i in self.ISIMM.Etudiants:
            if(i.niveauEtude==self.comboBoxNiveau2.currentText() and i.section==self.comboBoxSection2.currentText()):
                self.comboBoxEtudiantSectionNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)            
    def radioToggle(self,radio):
        if(radio==self.SupprimerEtudiant):
            self.comboBoxEtudiant.setVisible(True)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.comboBoxSection1.setVisible(False)
            self.comboBoxNiveau1.setVisible(False)
            self.comboBoxNiveau2.setVisible(False)
            self.comboBoxSection2.setVisible(False)

            self.comboBoxEtudiant.clear()
            for i in self.ISIMM.Etudiants:
                self.comboBoxEtudiant.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        elif(radio==self.SupprimerEtudiantSection):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(True)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.comboBoxSection1.setVisible(True)
            self.comboBoxNiveau1.setVisible(False)
            self.comboBoxNiveau2.setVisible(False)
            self.comboBoxSection2.setVisible(False)
            self.comboBoxEtudiantSection.clear()
            for i in self.ISIMM.Etudiants:
                if(i.section=="Cycle preparatoire integre (CPI)"):
                    self.comboBoxEtudiantSection.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        elif(radio==self.SupprimerEtudiantNiveau):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(True)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.comboBoxSection1.setVisible(False)
            self.comboBoxNiveau1.setVisible(True)
            self.comboBoxNiveau2.setVisible(False)
            self.comboBoxSection2.setVisible(False)
            self.comboBoxEtudiantNiveau.clear()
            for i in self.ISIMM.Etudiants:
                if(i.niveauEtude=="1"):
                    self.comboBoxEtudiantNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
        elif(radio==self.SupprimerEtudiantSectionNiveau):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(True)

            self.comboBoxSection1.setVisible(False)
            self.comboBoxNiveau1.setVisible(False)
            self.comboBoxNiveau2.setVisible(True)
            self.comboBoxSection2.setVisible(True)
            self.comboBoxEtudiantSectionNiveau.clear()
            for i in self.ISIMM.Etudiants:
                if(i.section=="Cycle preparatoire integre (CPI)" and i.niveauEtude=="1"):
                    self.comboBoxEtudiantSectionNiveau.addItem(i.nInscription+" "+i.nom+" "+i.prenom)
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
        Dialog.resize(1103, 782)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.Supprimer = QtWidgets.QPushButton(Dialog)
        self.Supprimer.setGeometry(QtCore.QRect(380, 700, 351, 41))
        self.Supprimer.setObjectName("Supprimer")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(380, 30, 291, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.comboBoxEtudiant = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiant.setGeometry(QtCore.QRect(470, 200, 271, 31))
        self.comboBoxEtudiant.setObjectName("comboBoxEtudiant")
        self.comboBoxEtudiantSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantSection.setGeometry(QtCore.QRect(770, 291, 271, 31))
        self.comboBoxEtudiantSection.setObjectName("comboBoxEtudiantSection")
        self.comboBoxEtudiantNiveau = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantNiveau.setGeometry(QtCore.QRect(770, 392, 271, 31))
        self.comboBoxEtudiantNiveau.setObjectName("comboBoxEtudiantNiveau")
        self.comboBoxEtudiantSectionNiveau = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantSectionNiveau.setGeometry(QtCore.QRect(770, 482, 271, 31))
        self.comboBoxEtudiantSectionNiveau.setObjectName("comboBoxEtudiantSectionNiveau")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 140, 381, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SupprimerEtudiant = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerEtudiant.setObjectName("SupprimerEtudiant")
        self.verticalLayout.addWidget(self.SupprimerEtudiant)
        self.SupprimerEtudiantSection = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerEtudiantSection.setObjectName("SupprimerEtudiantSection")
        self.verticalLayout.addWidget(self.SupprimerEtudiantSection)
        self.SupprimerEtudiantNiveau = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerEtudiantNiveau.setObjectName("SupprimerEtudiantNiveau")
        self.verticalLayout.addWidget(self.SupprimerEtudiantNiveau)
        self.SupprimerEtudiantSectionNiveau = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerEtudiantSectionNiveau.setObjectName("SupprimerEtudiantSectionNiveau")
        self.verticalLayout.addWidget(self.SupprimerEtudiantSectionNiveau)
        self.comboBoxSection1 = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection1.setGeometry(QtCore.QRect(470, 290, 271, 31))
        self.comboBoxSection1.setObjectName("comboBoxSection1")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.comboBoxNiveau1 = QtWidgets.QComboBox(Dialog)
        self.comboBoxNiveau1.setGeometry(QtCore.QRect(470, 390, 271, 31))
        self.comboBoxNiveau1.setObjectName("comboBoxNiveau1")
        self.comboBoxNiveau1.addItem("")
        self.comboBoxNiveau1.addItem("")
        self.comboBoxNiveau1.addItem("")
        self.comboBoxNiveau2 = QtWidgets.QComboBox(Dialog)
        self.comboBoxNiveau2.setGeometry(QtCore.QRect(470, 480, 51, 31))
        self.comboBoxNiveau2.setObjectName("comboBoxNiveau2")
        self.comboBoxNiveau2.addItem("")
        self.comboBoxNiveau2.addItem("")
        self.comboBoxNiveau2.addItem("")
        self.comboBoxSection2 = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection2.setGeometry(QtCore.QRect(530, 480, 211, 31))
        self.comboBoxSection2.setObjectName("comboBoxSection2")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1211, 821))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.Supprimer.raise_()
        self.label_1.raise_()
        self.comboBoxEtudiant.raise_()
        self.comboBoxEtudiantSection.raise_()
        self.comboBoxEtudiantNiveau.raise_()
        self.comboBoxEtudiantSectionNiveau.raise_()
        self.layoutWidget.raise_()
        self.comboBoxSection1.raise_()
        self.comboBoxNiveau1.raise_()
        self.comboBoxNiveau2.raise_()
        self.comboBoxSection2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.comboBoxEtudiant.setVisible(False)
        self.comboBoxEtudiantSection.setVisible(False)
        self.comboBoxEtudiantNiveau.setVisible(False)
        self.comboBoxEtudiantSectionNiveau.setVisible(False)

        self.comboBoxSection1.setVisible(False)
        self.comboBoxNiveau1.setVisible(False)
        self.comboBoxNiveau2.setVisible(False)
        self.comboBoxSection2.setVisible(False)

        self.SupprimerEtudiant.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiant))
        self.SupprimerEtudiantSection.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantSection))
        self.SupprimerEtudiantNiveau.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantNiveau))
        self.SupprimerEtudiantSectionNiveau.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantSectionNiveau))

        self.comboBoxSection1.currentIndexChanged.connect(self.comboSectionChanged)
        self.comboBoxNiveau1.currentIndexChanged.connect(self.comboNiveauChanged)

        self.comboBoxNiveau2.currentIndexChanged.connect(self.comboSectionNiveauChanged)
        self.comboBoxSection2.currentIndexChanged.connect(self.comboSectionNiveauChanged)

        self.Supprimer.clicked.connect(self.deleteEtudiant)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Supprimer.setText(_translate("Dialog", "Supprimer"))
        self.label_1.setText(_translate("Dialog", "Supprimer un étudiant"))
        self.SupprimerEtudiant.setText(_translate("Dialog", "Supprimer un étudiant"))
        self.SupprimerEtudiantSection.setText(_translate("Dialog", "Supprimer un étudiant d\'une section"))
        self.SupprimerEtudiantNiveau.setText(_translate("Dialog", "Supprimer un étudiant d\'un niveau"))
        self.SupprimerEtudiantSectionNiveau.setText(_translate("Dialog", "Supprimer un étudiant d\'une section et d\'un niveau "))
        self.comboBoxSection1.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection1.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection1.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBoxSection1.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.comboBoxNiveau1.setItemText(0, _translate("Dialog", "1"))
        self.comboBoxNiveau1.setItemText(1, _translate("Dialog", "2"))
        self.comboBoxNiveau1.setItemText(2, _translate("Dialog", "3"))
        self.comboBoxNiveau2.setItemText(0, _translate("Dialog", "1"))
        self.comboBoxNiveau2.setItemText(1, _translate("Dialog", "2"))
        self.comboBoxNiveau2.setItemText(2, _translate("Dialog", "3"))
        self.comboBoxSection2.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection2.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection2.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBoxSection2.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
import Backgrounds
