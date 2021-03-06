from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["Code","Designation","Semestre","Coefficient","Section"]
        

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
        return 5

class Ui_Dialog(object):
    def comboChanged(self):
        self.modal.deleteLater()
        alternative=[]
        for matiere in self.ISIMM.Matieres:
            if(matiere.section==self.comboBoxSection.currentText() and matiere.semestre==self.comboBoxSemestre.currentText()):
                alternative.append([matiere.code,matiere.designation,matiere.semestre,matiere.coefficient,matiere.section])
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
        Dialog.resize(1156, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.comboBoxSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection.setGeometry(QtCore.QRect(230, 170, 271, 31))
        self.comboBoxSection.setObjectName("comboBoxSection")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSemestre = QtWidgets.QComboBox(Dialog)
        self.comboBoxSemestre.setGeometry(QtCore.QRect(600, 170, 271, 31))
        self.comboBoxSemestre.setObjectName("comboBoxSemestre")
        self.comboBoxSemestre.addItem("")
        self.comboBoxSemestre.addItem("")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 230, 1161, 551))
        self.tableView.setObjectName("tableView")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(340, 50, 451, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1291, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.comboBoxSection.raise_()
        self.comboBoxSemestre.raise_()
        self.tableView.raise_()
        self.label_10.raise_()
        self.tableView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(1, 255, 255,255), stop:1 rgba(255, 255, 255, 255));")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        alternative=[]
        for matiere in self.ISIMM.Matieres:
            if(matiere.section==self.comboBoxSection.currentText() and matiere.semestre==self.comboBoxSemestre.currentText()):
                alternative.append([matiere.code,matiere.designation,matiere.semestre,matiere.coefficient,matiere.section])

        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.comboBoxSection.currentTextChanged.connect(self.comboChanged)
        self.comboBoxSemestre.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBoxSection.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection.setItemText(2, _translate("Dialog", "Licence en sciences de linformatique(L-I)"))
        self.comboBoxSection.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.comboBoxSemestre.setItemText(0, _translate("Dialog", "S1"))
        self.comboBoxSemestre.setItemText(1, _translate("Dialog", "S2"))
        self.label_10.setText(_translate("Dialog", "Recherche par Section et Semestre"))
import Backgrounds
