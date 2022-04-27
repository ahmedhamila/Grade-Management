from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns=["N inscription","Nom","Prenom","Date de Naissance","Section","Niveau","Moyenne"]
        

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
    def comboChanged(self):
        self.modal.deleteLater()
        alternative=[]
        for etudiant in self.ISIMM.Etudiants:
            if(etudiant.section==self.comboBoxSection.currentText()):
                somme_coeff=0
                somme_moyenne=0
                for note in self.ISIMM.Notes:
                    if(note.nInscription==etudiant.nInscription):
                        somme_coeff+=float(self.ISIMM.getMatiere(note.code).coefficient)
                        somme_moyenne+=self.ISIMM.moyenne(note.noteDS,note.noteEX)*float(self.ISIMM.getMatiere(note.code).coefficient)
                if(somme_coeff!=0 and somme_moyenne/somme_coeff >=10 ):
                    alternative.append([etudiant.nInscription,etudiant.nom,etudiant.prenom,etudiant.dateN,etudiant.section,etudiant.niveauEtude,str(somme_moyenne/somme_coeff)])

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
        Dialog.resize(1158, 808)
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
        self.comboBoxSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection.setGeometry(QtCore.QRect(220, 90, 301, 31))
        self.comboBoxSection.setObjectName("comboBoxSection")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(340, 30, 451, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 150, 1161, 631))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1371, 871))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.comboBoxSection.raise_()
        self.label_10.raise_()
        self.tableView.raise_()
        self.tableView.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(1, 255, 255,255), stop:1 rgba(255, 255, 255, 255));")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        alternative=[]
        for etudiant in self.ISIMM.Etudiants:
            if(etudiant.section==self.comboBoxSection.currentText()):
                somme_coeff=0
                somme_moyenne=0
                for note in self.ISIMM.Notes:
                    if(note.nInscription==etudiant.nInscription):
                        somme_coeff+=float(self.ISIMM.getMatiere(note.code).coefficient)
                        somme_moyenne+=self.ISIMM.moyenne(note.noteDS,note.noteEX)*float(self.ISIMM.getMatiere(note.code).coefficient)
                if(somme_coeff!=0 and somme_moyenne/somme_coeff >=10 ):
                    alternative.append([etudiant.nInscription,etudiant.nom,etudiant.prenom,etudiant.dateN,etudiant.section,etudiant.niveauEtude,str(round(somme_moyenne/somme_coeff,2))])

        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.comboBoxSection.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Section"))
        self.label.setText(_translate("Dialog", "Année scolaire 2021/2022"))
        self.comboBoxSection.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBoxSection.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))
        self.label_10.setText(_translate("Dialog", "Les Etudiants Admis d\'une Section"))
import Backgrounds
