from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(object):
    def deleteMatiere(self):
        if(self.SupprimerMatiere.isChecked()):
            code=self.comboBoxMatiere.currentText().split(" ")[0]
            if(self.ISIMM.getMatiere(code)!=False):
                self.ISIMM.Matieres.remove(self.ISIMM.getMatiere(code))
            self.comboBoxMatiere.clear()
            for i in self.ISIMM.Matieres:
                self.comboBoxMatiere.addItem(i.code+" "+i.designation)
        if(self.SupprimerMatiereSection.isChecked()):
            code=self.comboBoxMatiereSection.currentText().split(" ")[0]
            if(self.ISIMM.getMatiere(code)!=False):
                self.ISIMM.Matieres.remove(self.ISIMM.getMatiere(code))
            self.comboBoxMatiereSection.clear()
            for i in self.ISIMM.Matieres:
                if(i.section==self.comboBoxSection1.currentText()):
                    self.comboBoxMatiereSection.addItem(i.code+" "+i.designation)

        if(self.SupprimerMatiereSectionSemestre.isChecked()):
            code=self.comboBoxMatiereSectionSemestre.currentText().split(" ")[0]
            if(self.ISIMM.getMatiere(code)!=False):
                self.ISIMM.Matieres.remove(self.ISIMM.getMatiere(code))
            self.comboBoxMatiereSectionSemestre.clear()
            for i in self.ISIMM.Matieres:
                if(i.semestre==self.comboBoxSemestre.currentText() and i.section==self.comboBoxSection2.currentText()):
                    self.comboBoxMatiereSectionSemestre.addItem(i.code+" "+i.designation)
    
    def comboSectionChanged(self):
        self.comboBoxMatiereSection.clear()
        for i in self.ISIMM.Matieres:
            if(i.section==self.comboBoxSection1.currentText()):
                self.comboBoxMatiereSection.addItem(i.code+" "+i.designation)
    def comboSectionSemestreChanged(self):
        self.comboBoxMatiereSectionSemestre.clear()
        for i in self.ISIMM.Matieres:
            if(i.semestre==self.comboBoxSemestre.currentText() and i.section==self.comboBoxSection2.currentText()):
                self.comboBoxMatiereSectionSemestre.addItem(i.code+" "+i.designation) 

    def radioToggle(self,radio):
        if(radio==self.SupprimerMatiere):
            self.comboBoxMatiere.setVisible(True)
            self.comboBoxMatiereSection.setVisible(False)
            self.comboBoxMatiereSectionSemestre.setVisible(False)

            self.comboBoxSection1.setVisible(False)
            self.comboBoxSection2.setVisible(False)
            self.comboBoxSemestre.setVisible(False)

            self.comboBoxMatiere.clear()
            for i in self.ISIMM.Matieres:
                self.comboBoxMatiere.addItem(i.code+" "+i.designation)
        elif(radio==self.SupprimerMatiereSection):
            self.comboBoxMatiere.setVisible(False)
            self.comboBoxMatiereSection.setVisible(True)
            self.comboBoxMatiereSectionSemestre.setVisible(False)

            self.comboBoxSection1.setVisible(True)
            self.comboBoxSection2.setVisible(False)
            self.comboBoxSemestre.setVisible(False)
            self.comboBoxMatiereSection.clear()
            for i in self.ISIMM.Matieres:
                if(i.section=="Cycle preparatoire integre (CPI)"):
                    self.comboBoxMatiereSection.addItem(i.code+" "+i.designation)

        elif(radio==self.SupprimerMatiereSectionSemestre):
            self.comboBoxMatiere.setVisible(False)
            self.comboBoxMatiereSection.setVisible(False)
            self.comboBoxMatiereSectionSemestre.setVisible(True)

            self.comboBoxSection1.setVisible(False)
            self.comboBoxSection2.setVisible(True)
            self.comboBoxSemestre.setVisible(True)
            self.comboBoxMatiereSectionSemestre.clear()
            for i in self.ISIMM.Matieres:
                if(i.section=="Cycle preparatoire integre (CPI)" and i.semestre=="S1"):
                    self.comboBoxMatiereSectionSemestre.addItem(i.code+" "+i.designation)

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
        Dialog.resize(1156, 809)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.comboBoxMatiereSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiereSection.setGeometry(QtCore.QRect(810, 341, 271, 31))
        self.comboBoxMatiereSection.setObjectName("comboBoxMatiereSection")
        self.comboBoxSection1 = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection1.setGeometry(QtCore.QRect(510, 340, 271, 31))
        self.comboBoxSection1.setObjectName("comboBoxSection1")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.comboBoxSection1.addItem("")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(420, 30, 291, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.comboBoxMatiereSectionSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiereSectionSemestre.setGeometry(QtCore.QRect(810, 462, 271, 31))
        self.comboBoxMatiereSectionSemestre.setObjectName("comboBoxMatiereSectionSemestre")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 140, 381, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SupprimerMatiere = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerMatiere.setObjectName("SupprimerMatiere")
        self.verticalLayout.addWidget(self.SupprimerMatiere)
        self.SupprimerMatiereSection = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerMatiereSection.setObjectName("SupprimerMatiereSection")
        self.verticalLayout.addWidget(self.SupprimerMatiereSection)
        self.SupprimerMatiereSectionSemestre = QtWidgets.QRadioButton(self.layoutWidget)
        self.SupprimerMatiereSectionSemestre.setObjectName("SupprimerMatiereSectionSemestre")
        self.verticalLayout.addWidget(self.SupprimerMatiereSectionSemestre)
        self.comboBoxMatiere = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiere.setGeometry(QtCore.QRect(510, 230, 271, 31))
        self.comboBoxMatiere.setObjectName("comboBoxMatiere")
        self.comboBoxSection2 = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection2.setGeometry(QtCore.QRect(570, 460, 211, 31))
        self.comboBoxSection2.setObjectName("comboBoxSection2")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.comboBoxSection2.addItem("")
        self.Supprimer = QtWidgets.QPushButton(Dialog)
        self.Supprimer.setGeometry(QtCore.QRect(420, 700, 351, 41))
        self.Supprimer.setObjectName("Supprimer")
        self.comboBoxSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxSemestre.setGeometry(QtCore.QRect(510, 460, 51, 31))
        self.comboBoxSemestre.setObjectName("comboBoxSemestre")
        self.comboBoxSemestre.addItem("")
        self.comboBoxSemestre.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1261, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.comboBoxMatiereSection.raise_()
        self.comboBoxSection1.raise_()
        self.label_1.raise_()
        self.comboBoxMatiereSectionSemestre.raise_()
        self.layoutWidget.raise_()
        self.comboBoxMatiere.raise_()
        self.comboBoxSection2.raise_()
        self.Supprimer.raise_()
        self.comboBoxSemestre.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        self.comboBoxMatiere.setVisible(False)
        self.comboBoxMatiereSection.setVisible(False)
        self.comboBoxMatiereSectionSemestre.setVisible(False)

        self.comboBoxSection1.setVisible(False)
        self.comboBoxSection2.setVisible(False)
        self.comboBoxSemestre.setVisible(False)

        self.SupprimerMatiere.toggled.connect(lambda : self.radioToggle(self.SupprimerMatiere))
        self.SupprimerMatiereSection.toggled.connect(lambda : self.radioToggle(self.SupprimerMatiereSection))
        self.SupprimerMatiereSectionSemestre.toggled.connect(lambda : self.radioToggle(self.SupprimerMatiereSectionSemestre))

        self.comboBoxSection1.currentTextChanged.connect(self.comboSectionChanged)
        self.comboBoxSection2.currentTextChanged.connect(self.comboSectionSemestreChanged)
        self.comboBoxSemestre.currentTextChanged.connect(self.comboSectionSemestreChanged)

        self.Supprimer.clicked.connect(self.deleteMatiere)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBoxSection1.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection1.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection1.setItemText(2, _translate("Dialog", "Licence en sciences de linformatique(L-I)"))
        self.comboBoxSection1.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.label_1.setText(_translate("Dialog", "Supprimer une matiére"))
        self.SupprimerMatiere.setText(_translate("Dialog", "Supprimer une matiére"))
        self.SupprimerMatiereSection.setText(_translate("Dialog", "Supprimer une matiére par Section"))
        self.SupprimerMatiereSectionSemestre.setText(_translate("Dialog", "Supprimer une matiére par Section et Semestre"))
        self.comboBoxSection2.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection2.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection2.setItemText(2, _translate("Dialog", "Licence en sciences de linformatique(L-I)"))
        self.comboBoxSection2.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.Supprimer.setText(_translate("Dialog", "Supprimer"))
        self.comboBoxSemestre.setItemText(0, _translate("Dialog", "S1"))
        self.comboBoxSemestre.setItemText(1, _translate("Dialog", "S2"))
import Backgrounds
