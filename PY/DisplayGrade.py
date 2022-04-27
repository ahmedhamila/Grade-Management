from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

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
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1156, 808)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 150, 1161, 661))
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setObjectName("tableView")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(410, 60, 251, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.tableView.raise_()
        self.label_10.raise_()
        self.tableView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(1, 255, 255,255), stop:1 rgba(255, 255, 255, 255));")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        alternative=[]
        for note in self.ISIMM.Notes:
            alternative.append([note.nInscription,self.ISIMM.getEtudiant(note.nInscription).nom,self.ISIMM.getEtudiant(note.nInscription).prenom,note.code,self.ISIMM.getMatiere(note.code).designation,note.noteDS,note.noteEX])

        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Affichage des notes"))
import Backgrounds
