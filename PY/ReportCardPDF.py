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
    def __init__(self,ISIMM,nInscr):
        self.ISIMM=ISIMM
        self.nInscr=nInscr

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1179, 988)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1181, 1231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(830, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 191, 31))
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
        self.label_5.setGeometry(QtCore.QRect(10, 220, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(440, 20, 311, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.labelNomDateN = QtWidgets.QLabel(Dialog)
        self.labelNomDateN.setGeometry(QtCore.QRect(190, 220, 191, 31))
        self.labelNomDateN.setStyleSheet("font: 75 19pt \"MS Sans Serif\";")
        self.labelNomDateN.setText("")
        self.labelNomDateN.setObjectName("labelNomDateN")
        self.labelNomSection = QtWidgets.QLabel(Dialog)
        self.labelNomSection.setGeometry(QtCore.QRect(100, 170, 400, 31))
        self.labelNomSection.setStyleSheet("font: 75 19pt \"MS Sans Serif\";")
        self.labelNomSection.setText("")
        self.labelNomSection.setObjectName("labelNomSection")
        self.labelNomPrenom = QtWidgets.QLabel(Dialog)
        self.labelNomPrenom.setGeometry(QtCore.QRect(170, 120, 191, 31))
        self.labelNomPrenom.setStyleSheet("font: 75 19pt \"MS Sans Serif\";")
        self.labelNomPrenom.setText("")
        self.labelNomPrenom.setObjectName("labelNomPrenom")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(830, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.labelAdresse = QtWidgets.QLabel(Dialog)
        self.labelAdresse.setGeometry(QtCore.QRect(910, 120, 191, 31))
        self.labelAdresse.setStyleSheet("font: 75 19pt \"MS Sans Serif\";")
        self.labelAdresse.setText("")
        self.labelAdresse.setObjectName("labelAdresse")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.labelNInscription = QtWidgets.QLabel(Dialog)
        self.labelNInscription.setGeometry(QtCore.QRect(210, 80, 191, 31))
        self.labelNInscription.setStyleSheet("font: 75 19pt \"MS Sans Serif\";")
        self.labelNInscription.setText("")
        self.labelNInscription.setObjectName("labelNInscription")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(30, 330, 1101, 641))
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(1, 255, 255,255), stop:1 rgba(255, 255, 255, 255));")
        self.tableView.setMidLineWidth(0)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.labelNInscription.setText(self.nInscr)
        self.labelAdresse.setText(self.ISIMM.getEtudiant(self.nInscr).adresse)
        self.labelNomPrenom.setText(self.ISIMM.getEtudiant(self.nInscr).nom+" "+self.ISIMM.getEtudiant(self.nInscr).prenom)
        self.labelNomSection.setText(self.ISIMM.getEtudiant(self.nInscr).section)
        self.labelNomDateN.setText(str(self.ISIMM.getEtudiant(self.nInscr).dateN.year())+"/"+str(self.ISIMM.getEtudiant(self.nInscr).dateN.month())+"/"+str(self.ISIMM.getEtudiant(self.nInscr).dateN.day()))
            
        alternative=[]
        somme_coeff=0
        somme_moyenne=0
        for note in self.ISIMM.Notes:
            if(note.nInscription==self.nInscr):
                alternative.append([note.code +" "+self.ISIMM.getMatiere(note.code).designation,self.ISIMM.getMatiere(note.code).coefficient,note.noteDS,note.noteEX,str(round(self.ISIMM.moyenne(note.noteDS,note.noteEX),2)),str(self.ISIMM.rang(self.ISIMM.getEtudiant(note.nInscription),self.ISIMM.getMatiere(note.code)))])
                somme_coeff+=float(self.ISIMM.getMatiere(note.code).coefficient)
                somme_moyenne+=self.ISIMM.moyenne(note.noteDS,note.noteEX)*float(self.ISIMM.getMatiere(note.code).coefficient)
        if(somme_coeff!=0 and somme_moyenne!=0):
            alternative.append(["Total",str(somme_coeff),"----","----",str(round(somme_moyenne/somme_coeff,2)),"---"])
        self.modal=TableModel(alternative)
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Section :"))
        self.label_2.setText(_translate("Dialog", "Adresse:"))
        self.label_6.setText(_translate("Dialog", "Numero d\'inscription :"))
        self.label_5.setText(_translate("Dialog", "Date de naissance :"))
        self.label_10.setText(_translate("Dialog", "Bulletin de note"))
        self.label_3.setText(_translate("Dialog", "Année scolaire 2021/2022"))
        self.label_7.setText(_translate("Dialog", "Nom et Prénom :"))
import Backgrounds
