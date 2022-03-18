from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(object):

    def radioToggle(self,radio):
        if(radio==self.SupprimerEtudiant):
            self.comboBoxEtudiant.setVisible(True)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.lineEditSection.setVisible(False)
            self.lineEditNiveau.setVisible(False)
            self.lineEditSectionNiveau1.setVisible(False)
            self.lineEditSectionNiveau2.setVisible(False)
        elif(radio==self.SupprimerEtudiantSection):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(True)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.lineEditSection.setVisible(True)
            self.lineEditNiveau.setVisible(False)
            self.lineEditSectionNiveau1.setVisible(False)
            self.lineEditSectionNiveau2.setVisible(False)
        elif(radio==self.SupprimerEtudiantNiveau):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(True)
            self.comboBoxEtudiantSectionNiveau.setVisible(False)

            self.lineEditSection.setVisible(False)
            self.lineEditNiveau.setVisible(True)
            self.lineEditSectionNiveau1.setVisible(False)
            self.lineEditSectionNiveau2.setVisible(False)
        elif(radio==self.SupprimerEtudiantSectionNiveau):
            self.comboBoxEtudiant.setVisible(False)
            self.comboBoxEtudiantSection.setVisible(False)
            self.comboBoxEtudiantNiveau.setVisible(False)
            self.comboBoxEtudiantSectionNiveau.setVisible(True)

            self.lineEditSection.setVisible(False)
            self.lineEditNiveau.setVisible(False)
            self.lineEditSectionNiveau1.setVisible(True)
            self.lineEditSectionNiveau2.setVisible(True)

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
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.Ajouter = QtWidgets.QPushButton(Dialog)
        self.Ajouter.setGeometry(QtCore.QRect(380, 700, 351, 41))
        self.Ajouter.setObjectName("Ajouter")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(380, 30, 291, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.comboBoxEtudiant = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiant.setGeometry(QtCore.QRect(470, 200, 271, 31))
        self.comboBoxEtudiant.setObjectName("comboBoxEtudiant")
        self.lineEditSection = QtWidgets.QLineEdit(Dialog)
        self.lineEditSection.setGeometry(QtCore.QRect(470, 289, 271, 31))
        self.lineEditSection.setObjectName("lineEditSection")
        self.comboBoxEtudiantSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantSection.setGeometry(QtCore.QRect(770, 291, 271, 31))
        self.comboBoxEtudiantSection.setObjectName("comboBoxEtudiantSection")
        self.comboBoxEtudiantNiveau = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantNiveau.setGeometry(QtCore.QRect(770, 392, 271, 31))
        self.comboBoxEtudiantNiveau.setObjectName("comboBoxEtudiantNiveau")
        self.lineEditNiveau = QtWidgets.QLineEdit(Dialog)
        self.lineEditNiveau.setGeometry(QtCore.QRect(470, 390, 271, 31))
        self.lineEditNiveau.setObjectName("lineEditNiveau")
        self.comboBoxEtudiantSectionNiveau = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiantSectionNiveau.setGeometry(QtCore.QRect(770, 482, 271, 31))
        self.comboBoxEtudiantSectionNiveau.setObjectName("comboBoxEtudiantSectionNiveau")
        self.lineEditSectionNiveau1 = QtWidgets.QLineEdit(Dialog)
        self.lineEditSectionNiveau1.setGeometry(QtCore.QRect(470, 480, 131, 31))
        self.lineEditSectionNiveau1.setObjectName("lineEditSectionNiveau1")
        self.lineEditSectionNiveau2 = QtWidgets.QLineEdit(Dialog)
        self.lineEditSectionNiveau2.setGeometry(QtCore.QRect(610, 480, 131, 31))
        self.lineEditSectionNiveau2.setObjectName("lineEditSectionNiveau2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 140, 374, 431))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SupprimerEtudiant = QtWidgets.QRadioButton(self.widget)
        self.SupprimerEtudiant.setObjectName("SupprimerEtudiant")
        self.verticalLayout.addWidget(self.SupprimerEtudiant)
        self.SupprimerEtudiantSection = QtWidgets.QRadioButton(self.widget)
        self.SupprimerEtudiantSection.setObjectName("SupprimerEtudiantSection")
        self.verticalLayout.addWidget(self.SupprimerEtudiantSection)
        self.SupprimerEtudiantNiveau = QtWidgets.QRadioButton(self.widget)
        self.SupprimerEtudiantNiveau.setObjectName("SupprimerEtudiantNiveau")
        self.verticalLayout.addWidget(self.SupprimerEtudiantNiveau)
        self.SupprimerEtudiantSectionNiveau = QtWidgets.QRadioButton(self.widget)
        self.SupprimerEtudiantSectionNiveau.setObjectName("SupprimerEtudiantSectionNiveau")
        self.verticalLayout.addWidget(self.SupprimerEtudiantSectionNiveau)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.comboBoxEtudiant.setVisible(False)
        self.comboBoxEtudiantSection.setVisible(False)
        self.comboBoxEtudiantNiveau.setVisible(False)
        self.comboBoxEtudiantSectionNiveau.setVisible(False)

        self.lineEditSection.setVisible(False)
        self.lineEditNiveau.setVisible(False)
        self.lineEditSectionNiveau1.setVisible(False)
        self.lineEditSectionNiveau2.setVisible(False)

        self.SupprimerEtudiant.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiant))
        self.SupprimerEtudiantSection.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantSection))
        self.SupprimerEtudiantNiveau.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantNiveau))
        self.SupprimerEtudiantSectionNiveau.toggled.connect(lambda : self.radioToggle(self.SupprimerEtudiantSectionNiveau))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Ajouter.setText(_translate("Dialog", "Supprimer"))
        self.label_1.setText(_translate("Dialog", "Supprimer un étudiant"))
        self.SupprimerEtudiant.setText(_translate("Dialog", "Supprimer un étudiant"))
        self.SupprimerEtudiantSection.setText(_translate("Dialog", "Supprimer un étudiant d\'une section"))
        self.SupprimerEtudiantNiveau.setText(_translate("Dialog", "Supprimer un étudiant d\'un niveau"))
        self.SupprimerEtudiantSectionNiveau.setText(_translate("Dialog", "Supprimer un étudiant d\'une section et d\'un niveau "))
