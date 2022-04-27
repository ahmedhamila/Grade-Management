from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
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
        return 1

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 5

class Ui_Dialog(object):
    def afficherRecherche(self):

        code=self.lineEditNumeroInscription.text()
        if(not (code.isnumeric() and len(code)>=4)):
            self.showDialog("Invalid Input","Code doit etre numerique de taille minimum 4",True)
            self.lineEditNumeroInscription.setText("")
            if(not self.empty):
                self.modal.deleteLater()
                self.empty=True
            return
        alternative=[]
        for matiere in self.ISIMM.Matieres:
            if(matiere.code==code):
                alternative.append([matiere.code,matiere.designation,matiere.semestre,matiere.coefficient,matiere.section])
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
    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1157, 809)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 450, 1161, 192))
        self.tableView.setObjectName("tableView")
        self.lineEditNumeroInscription = QtWidgets.QLineEdit(Dialog)
        self.lineEditNumeroInscription.setGeometry(QtCore.QRect(420, 230, 421, 30))
        self.lineEditNumeroInscription.setInputMask("")
        self.lineEditNumeroInscription.setMaxLength(32767)
        self.lineEditNumeroInscription.setObjectName("lineEditNumeroInscription")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 261, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.Search = QtWidgets.QPushButton(Dialog)
        self.Search.setGeometry(QtCore.QRect(380, 340, 351, 31))
        self.Search.setObjectName("Search")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 230, 161, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1291, 871))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.tableView.raise_()
        self.lineEditNumeroInscription.raise_()
        self.label_10.raise_()
        self.Search.raise_()
        self.label.raise_()
        self.tableView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(1, 255, 255,255), stop:1 rgba(255, 255, 255, 255));")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.empty=True
        
        self.Search.clicked.connect(self.afficherRecherche)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Recherche par Code"))
        self.Search.setText(_translate("Dialog", "Rechercher"))
        self.label.setText(_translate("Dialog", "Recherche par Code"))
import Backgrounds
