
from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import *
class Ui_Dialog(object):
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
        

    def comboChanged(self):
        code=self.comboBoxMatiere.currentText().split(" ")[3]
        nInscr=self.comboBoxMatiere.currentText().split(" ")[0]
        if(self.ISIMM.getNote(code,nInscr)!=False):
            self.lineNoteDS.setText(self.ISIMM.getNote(code,nInscr).noteDS)
            self.lineNoteEX.setText(self.ISIMM.getNote(code,nInscr).noteEX)
    def modifier(self):
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
        self.showDialog("Success","Modification Effectué avec succée",False)
        code=self.comboBoxMatiere.currentText().split(" ")[3]
        nInscr=self.comboBoxMatiere.currentText().split(" ")[0]
        self.ISIMM.getNote(code,nInscr).noteDS=noteD
        self.ISIMM.getNote(code,nInscr).noteEX=noteE

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
        Dialog.resize(1102, 778)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(440, 30, 261, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 210, 211, 31))
        self.label.setObjectName("label")
        self.comboBoxMatiere = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiere.setGeometry(QtCore.QRect(490, 210, 421, 31))
        self.comboBoxMatiere.setObjectName("comboBoxMatiere")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(200, 370, 161, 21))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.lineNoteDS = QtWidgets.QLineEdit(Dialog)
        self.lineNoteDS.setGeometry(QtCore.QRect(490, 370, 421, 30))
        self.lineNoteDS.setObjectName("lineNoteDS")
        self.Modifier = QtWidgets.QPushButton(Dialog)
        self.Modifier.setGeometry(QtCore.QRect(360, 610, 351, 31))
        self.Modifier.setObjectName("Modifier")
        self.lineNoteEX = QtWidgets.QLineEdit(Dialog)
        self.lineNoteEX.setGeometry(QtCore.QRect(490, 440, 421, 30))
        self.lineNoteEX.setObjectName("lineNoteEX")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(200, 440, 161, 21))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.comboBoxMatiere.clear()
        for note in self.ISIMM.Notes:
            self.comboBoxMatiere.addItem(note.nInscription+" "+self.ISIMM.getEtudiant(note.nInscription).nom+" "+self.ISIMM.getEtudiant(note.nInscription).prenom+" "+note.code+" "+self.ISIMM.getMatiere(note.code).designation)
    
        self.comboChanged()    
        self.comboBoxMatiere.currentTextChanged.connect(self.comboChanged)
        self.Modifier.clicked.connect(self.modifier)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Modifier une note"))
        self.label.setText(_translate("Dialog", "Selectionner une note"))
        self.label_8.setText(_translate("Dialog", "Note DS"))
        self.Modifier.setText(_translate("Dialog", "Modifier"))
        self.label_11.setText(_translate("Dialog", "Note EX"))
