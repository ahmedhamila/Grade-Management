from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
class Ui_Dialog(object):
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
        

    def comboChanged(self):
        code=self.comboBoxMatiere.currentText().split(" ")[0]
        if(self.ISIMM.getMatiere(code)!=False):
            self.lineEditDesignation.setText(self.ISIMM.getMatiere(code).designation)
            self.comboBoxCoefficient.setCurrentText(self.ISIMM.getMatiere(code).coefficient)
    def modifier(self):
        if len(self.ISIMM.Matieres):    
            design=self.lineEditDesignation.text()
            coeff=self.comboBoxCoefficient.currentText()
            if(not (len(design)>=3)):
                self.showDialog("Invalid Input","Designaion doit etre de taille minimimum 3",True)
                return
            self.showDialog("Success","Modification Effectué avec succée",False)
            code=self.comboBoxMatiere.currentText().split(" ")[0]
            self.ISIMM.getMatiere(code).designation=design
            self.ISIMM.getMatiere(code).coefficient=coeff
        else :
            self.lineEditDesignation.setDisabled(True)
            self.comboBoxCoefficient.setDisabled(True)
        

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
        Dialog.resize(1155, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(390, 30, 291, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.Modifier = QtWidgets.QPushButton(Dialog)
        self.Modifier.setGeometry(QtCore.QRect(390, 700, 351, 31))
        self.Modifier.setObjectName("Modifier")
        self.lineEditDesignation = QtWidgets.QLineEdit(Dialog)
        self.lineEditDesignation.setGeometry(QtCore.QRect(450, 410, 421, 30))
        self.lineEditDesignation.setObjectName("lineEditDesignation")
        self.comboBoxMatiere = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiere.setGeometry(QtCore.QRect(450, 200, 421, 31))
        self.comboBoxMatiere.setObjectName("comboBoxMatiere")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 190, 181, 41))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 410, 161, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.comboBoxCoefficient = QtWidgets.QComboBox(Dialog)
        self.comboBoxCoefficient.setGeometry(QtCore.QRect(450, 480, 421, 31))
        self.comboBoxCoefficient.setObjectName("comboBoxCoefficient")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.comboBoxCoefficient.addItem("")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(250, 480, 161, 21))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1341, 881))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_1.raise_()
        self.Modifier.raise_()
        self.lineEditDesignation.raise_()
        self.comboBoxMatiere.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.comboBoxCoefficient.raise_()
        self.label_11.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        for matiere in self.ISIMM.Matieres:
            self.comboBoxMatiere.addItem(matiere.code+" "+matiere.designation)
        if len(self.ISIMM.Matieres):
            self.comboChanged() 
        else :
            self.lineEditDesignation.setDisabled(True)
            self.comboBoxCoefficient.setDisabled(True)
           
        self.comboBoxMatiere.currentTextChanged.connect(self.comboChanged)
        self.Modifier.clicked.connect(self.modifier)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Modifier une matière"))
        self.Modifier.setText(_translate("Dialog", "Modifier"))
        self.label.setText(_translate("Dialog", "Selectionner une matière"))
        self.label_5.setText(_translate("Dialog", "Désignation"))
        self.comboBoxCoefficient.setItemText(0, _translate("Dialog", "0.5"))
        self.comboBoxCoefficient.setItemText(1, _translate("Dialog", "1"))
        self.comboBoxCoefficient.setItemText(2, _translate("Dialog", "1.5"))
        self.comboBoxCoefficient.setItemText(3, _translate("Dialog", "2"))
        self.label_11.setText(_translate("Dialog", "Coefficient"))
import Backgrounds
