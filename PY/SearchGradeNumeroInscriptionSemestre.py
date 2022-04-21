from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Numero d'inscription","Nom","Prenom","Code Matiere","Designation","NoteDS","NoteEX"]
        

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
        return 7


class Ui_Dialog(object):
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def afficherRecherche(self):

        nInscr=self.lineEditNumeroInscription.text()
        if(not (nInscr.isnumeric() and len(nInscr)>=4)):
            self.showDialog("Invalid Input","Numero d'inscription doit etre numerique de taille minimum 4",True)
            self.lineEditNumeroInscription.setText("")
            if(not self.empty):
                self.modal.deleteLater()
                self.empty=True
            return
        alternative=[]
        for note in self.ISIMM.Notes:
            if(note.nInscription==nInscr and self.ISIMM.getMatiere(note.code).semestre==self.comboBoxSemestre.currentText()):
                alternative.append([note.nInscription,self.ISIMM.getEtudiant(note.nInscription).nom,self.ISIMM.getEtudiant(note.nInscription).prenom,note.code,self.ISIMM.getMatiere(note.code).designation,note.noteDS,note.noteEX])
        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.empty=False


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

    def comboChanged(self):
        nInscr=self.lineEditNumeroInscription.text()
        if not self.empty:
            self.modal.deleteLater()
        alternative=[]
        for note in self.ISIMM.Notes:
            if(note.nInscription==nInscr and self.ISIMM.getMatiere(note.code).semestre==self.comboBoxSemestre.currentText()):
                alternative.append([note.nInscription,self.ISIMM.getEtudiant(note.nInscription).nom,self.ISIMM.getEtudiant(note.nInscription).prenom,note.code,self.ISIMM.getMatiere(note.code).designation,note.noteDS,note.noteEX])
        self.modal=TableModel(alternative)
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1155, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.lineEditNumeroInscription = QtWidgets.QLineEdit(Dialog)
        self.lineEditNumeroInscription.setGeometry(QtCore.QRect(420, 130, 421, 30))
        self.lineEditNumeroInscription.setInputMask("")
        self.lineEditNumeroInscription.setMaxLength(32767)
        self.lineEditNumeroInscription.setObjectName("lineEditNumeroInscription")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 130, 161, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.comboBoxSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxSemestre.setGeometry(QtCore.QRect(420, 210, 421, 31))
        self.comboBoxSemestre.setObjectName("comboBoxSemestre")
        self.comboBoxSemestre.addItem("")
        self.comboBoxSemestre.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 210, 161, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(250, 40, 621, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 340, 1161, 441))
        self.tableView.setObjectName("tableView")
        self.Rechercher = QtWidgets.QPushButton(Dialog)
        self.Rechercher.setGeometry(QtCore.QRect(400, 280, 351, 41))
        self.Rechercher.setObjectName("Rechercher")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1381, 881))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.lineEditNumeroInscription.raise_()
        self.label.raise_()
        self.comboBoxSemestre.raise_()
        self.label_2.raise_()
        self.label_10.raise_()
        self.tableView.raise_()
        self.Rechercher.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.empty=True
        self.Rechercher.clicked.connect(self.afficherRecherche)
        self.comboBoxSemestre.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Numéro d\'inscription"))
        self.comboBoxSemestre.setItemText(0, _translate("Dialog", "S1"))
        self.comboBoxSemestre.setItemText(1, _translate("Dialog", "S2"))
        self.label_2.setText(_translate("Dialog", "Semestre"))
        self.label_10.setText(_translate("Dialog", "Recherche par numero d\'inscription et semestre"))
        self.Rechercher.setText(_translate("Dialog", "Rechercher"))
import Backgrounds
