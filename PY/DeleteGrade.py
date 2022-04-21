from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def delete(self):
        if len(self.ISIMM.Notes)>0:
            code=self.comboBoxMatiere.currentText().split(" ")[3]
            nInscr=self.comboBoxMatiere.currentText().split(" ")[0]
            if(self.ISIMM.getNote(code,nInscr)!=False):
                self.ISIMM.Notes.remove(self.ISIMM.getNote(code,nInscr))
            self.comboBoxMatiere.clear()
            for note in self.ISIMM.Notes:
                self.comboBoxMatiere.addItem(note.nInscription+" "+self.ISIMM.getEtudiant(note.nInscription).nom+" "+self.ISIMM.getEtudiant(note.nInscription).prenom+" "+note.code+" "+self.ISIMM.getMatiere(note.code).designation)
            
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1156, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(440, 50, 261, 41))
        self.label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_1.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.comboBoxMatiere = QtWidgets.QComboBox(Dialog)
        self.comboBoxMatiere.setGeometry(QtCore.QRect(480, 310, 411, 31))
        self.comboBoxMatiere.setObjectName("comboBoxMatiere")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 310, 211, 31))
        self.label.setObjectName("label")
        self.Supprimer = QtWidgets.QPushButton(Dialog)
        self.Supprimer.setGeometry(QtCore.QRect(420, 640, 351, 41))
        self.Supprimer.setObjectName("Supprimer")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1261, 841))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_1.raise_()
        self.comboBoxMatiere.raise_()
        self.label.raise_()
        self.Supprimer.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.comboBoxMatiere.clear()
        for note in self.ISIMM.Notes:
            self.comboBoxMatiere.addItem(note.nInscription+" "+self.ISIMM.getEtudiant(note.nInscription).nom+" "+self.ISIMM.getEtudiant(note.nInscription).prenom+" "+note.code+" "+self.ISIMM.getMatiere(note.code).designation)
        self.Supprimer.clicked.connect(self.delete)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "Supprimer une note"))
        self.label.setText(_translate("Dialog", "Selectionner une note"))
        self.Supprimer.setText(_translate("Dialog", "Supprimer"))
import Backgrounds
