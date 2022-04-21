from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Matiere","Coefficient","Note DS","Note EX","Moyenne","Rang"]
        

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])

        

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 6


class Ui_Dialog(object):
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def comboChanged(self):
        self.modal.deleteLater()
        nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
        self.labelAdresse.setText(self.ISIMM.getEtudiant(nInscr).adresse)
        self.labelNomPrenom.setText(self.ISIMM.getEtudiant(nInscr).nom+" "+self.ISIMM.getEtudiant(nInscr).prenom)
        self.labelNomSection.setText(self.ISIMM.getEtudiant(nInscr).section)
        self.labelNomDateN.setText(self.ISIMM.getEtudiant(nInscr).dateN)
        alternative=[]
        somme_coeff=0
        somme_moyenne=0
        for note in self.ISIMM.Notes:
            if(note.nInscription==self.comboBoxEtudiant.currentText().split(" ")[0] and self.ISIMM.getMatiere(note.code).semestre==self.comboBoxSemestre.currentText()):
                alternative.append([note.code +" "+self.ISIMM.getMatiere(note.code).designation,self.ISIMM.getMatiere(note.code).coefficient,note.noteDS,note.noteEX,str(self.ISIMM.moyenne(note.noteDS,note.noteEX)),str(self.ISIMM.rang(self.ISIMM.getEtudiant(note.nInscription),self.ISIMM.getMatiere(note.code)))])
                somme_coeff+=float(self.ISIMM.getMatiere(note.code).coefficient)
                somme_moyenne+=self.ISIMM.moyenne(note.noteDS,note.noteEX)*float(self.ISIMM.getMatiere(note.code).coefficient)
        if(somme_coeff!=0 and somme_moyenne!=0):
            alternative.append(["Total",str(somme_coeff),"----","----",str(somme_moyenne/somme_coeff),"---"])
        self.modal=TableModel(alternative)
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1156, 835)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(830, 90, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.labelAdresse = QtWidgets.QLabel(Dialog)
        self.labelAdresse.setGeometry(QtCore.QRect(910, 140, 191, 31))
        self.labelAdresse.setText("")
        self.labelAdresse.setObjectName("labelAdresse")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 260, 1161, 521))
        self.tableView.setObjectName("tableView")
        self.labelNomSection = QtWidgets.QLabel(Dialog)
        self.labelNomSection.setGeometry(QtCore.QRect(100, 180, 271, 31))
        self.labelNomSection.setText("")
        self.labelNomSection.setObjectName("labelNomSection")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(380, 30, 391, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.labelNomPrenom = QtWidgets.QLabel(Dialog)
        self.labelNomPrenom.setGeometry(QtCore.QRect(170, 130, 191, 31))
        self.labelNomPrenom.setText("")
        self.labelNomPrenom.setObjectName("labelNomPrenom")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.comboBoxEtudiant = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiant.setGeometry(QtCore.QRect(220, 90, 301, 31))
        self.comboBoxEtudiant.setObjectName("comboBoxEtudiant")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(830, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.labelNomDateN = QtWidgets.QLabel(Dialog)
        self.labelNomDateN.setGeometry(QtCore.QRect(190, 230, 191, 31))
        self.labelNomDateN.setText("")
        self.labelNomDateN.setObjectName("labelNomDateN")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(540, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.comboBoxSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxSemestre.setGeometry(QtCore.QRect(630, 90, 171, 31))
        self.comboBoxSemestre.setObjectName("comboBoxSemestre")
        self.comboBoxSemestre.addItem("")
        self.comboBoxSemestre.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 1301, 881))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.labelAdresse.raise_()
        self.tableView.raise_()
        self.labelNomSection.raise_()
        self.label_10.raise_()
        self.labelNomPrenom.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.comboBoxEtudiant.raise_()
        self.label_2.raise_()
        self.labelNomDateN.raise_()
        self.label_7.raise_()
        self.comboBoxSemestre.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.comboBoxEtudiant.clear()

        for i in self.ISIMM.Etudiants:
            self.comboBoxEtudiant.addItem(i.nInscription+" "+i.nom+" "+i.prenom)

        if len(self.ISIMM.Etudiants)>0 :
            nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
            self.labelAdresse.setText(self.ISIMM.getEtudiant(nInscr).adresse)
            self.labelNomPrenom.setText(self.ISIMM.getEtudiant(nInscr).nom+" "+self.ISIMM.getEtudiant(nInscr).prenom)
            self.labelNomSection.setText(self.ISIMM.getEtudiant(nInscr).section)
            self.labelNomDateN.setText(self.ISIMM.getEtudiant(nInscr).dateN)
            alternative=[]
            somme_coeff=0
            somme_moyenne=0
            for note in self.ISIMM.Notes:
                if(note.nInscription==self.comboBoxEtudiant.currentText().split(" ")[0] and self.ISIMM.getMatiere(note.code).semestre==self.comboBoxSemestre.currentText()):
                    alternative.append([note.code +" "+self.ISIMM.getMatiere(note.code).designation,self.ISIMM.getMatiere(note.code).coefficient,note.noteDS,note.noteEX,str(self.ISIMM.moyenne(note.noteDS,note.noteEX)),str(self.ISIMM.rang(self.ISIMM.getEtudiant(note.nInscription),self.ISIMM.getMatiere(note.code)))])
                    somme_coeff+=float(self.ISIMM.getMatiere(note.code).coefficient)
                    somme_moyenne+=self.ISIMM.moyenne(note.noteDS,note.noteEX)*float(self.ISIMM.getMatiere(note.code).coefficient)
            if(somme_coeff!=0 and somme_moyenne!=0):
                alternative.append(["Total",str(somme_coeff),"----","----",str(somme_moyenne/somme_coeff),"---"])
            self.modal=TableModel(alternative)
            self.tableView.setModel(self.modal)
            self.horizontal_header = self.tableView.horizontalHeader()
            self.vertical_header = self.tableView.verticalHeader()
            self.horizontal_header.setSectionResizeMode(3)
            self.tableView.horizontalHeader().setStretchLastSection(True)
        self.comboBoxEtudiant.currentTextChanged.connect(self.comboChanged)
        self.comboBoxSemestre.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Numero d\'inscription"))
        self.label_5.setText(_translate("Dialog", "Date de naissance :"))
        self.label.setText(_translate("Dialog", "Année scolaire 2021/2022"))
        self.label_10.setText(_translate("Dialog", "Bulletin de note par semestre"))
        self.label_3.setText(_translate("Dialog", "Nom et Prénom :"))
        self.label_4.setText(_translate("Dialog", "Section :"))
        self.label_2.setText(_translate("Dialog", "Adresse:"))
        self.label_7.setText(_translate("Dialog", "Semestre"))
        self.comboBoxSemestre.setItemText(0, _translate("Dialog", "S1"))
        self.comboBoxSemestre.setItemText(1, _translate("Dialog", "S2"))
import Backgrounds
