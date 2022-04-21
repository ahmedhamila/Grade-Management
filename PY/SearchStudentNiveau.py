from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["N inscription","Nom","Prenom","Date de Naissance","Adresse","Mail","Telephone","Section","Niveau"]
        

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
        return 9

class Ui_Dialog(object):
    def comboChanged(self):
        self.modal.deleteLater()
        alternative=[]
        for etudiant in self.ISIMM.Etudiants:
            if(etudiant.niveauEtude==self.comboBox_2.currentText()):
                alternative.append([etudiant.nInscription,etudiant.nom,etudiant.prenom,etudiant.dateN,etudiant.adresse,etudiant.mail,etudiant.telephone,etudiant.section,etudiant.niveauEtude])
        self.modal=TableModel(alternative)
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1149, 809)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(410, 30, 291, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(240, 180, 161, 21))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 180, 421, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 290, 1151, 491))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1291, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.comboBox_2.raise_()
        self.tableView.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        alternative=[]
        for etudiant in self.ISIMM.Etudiants:
            if(etudiant.niveauEtude==self.comboBox_2.currentText()):
                alternative.append([etudiant.nInscription,etudiant.nom,etudiant.prenom,etudiant.dateN,etudiant.adresse,etudiant.mail,etudiant.telephone,etudiant.section,etudiant.niveauEtude])

        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.comboBox_2.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Recherche par Niveau"))
        self.label_9.setText(_translate("Dialog", "Niveau d\'étude"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "2"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "3"))
import Backgrounds
