# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SearchGradeSectionNiveau.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import imp
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
    def comboChanged(self):
        self.modal.deleteLater()
        alternative=[]
        for note in self.ISIMM.Notes:
            if(self.ISIMM.getEtudiant(note.nInscription).section==self.comboBoxSection.currentText() and self.ISIMM.getEtudiant(note.nInscription).niveauEtude==self.comboBoxNiveau.currentText()):
                alternative.append([note.nInscription,self.ISIMM.getEtudiant(note.nInscription).nom,self.ISIMM.getEtudiant(note.nInscription).prenom,note.code,self.ISIMM.getMatiere(note.code).designation,note.noteDS,note.noteEX])
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
        Dialog.resize(1102, 780)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.comboBoxNiveau = QtWidgets.QComboBox(Dialog)
        self.comboBoxNiveau.setGeometry(QtCore.QRect(600, 170, 271, 31))
        self.comboBoxNiveau.setObjectName("comboBoxNiveau")
        self.comboBoxNiveau.addItem("")
        self.comboBoxNiveau.addItem("")
        self.comboBoxNiveau.addItem("")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(350, 50, 421, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.comboBoxSection = QtWidgets.QComboBox(Dialog)
        self.comboBoxSection.setGeometry(QtCore.QRect(230, 170, 271, 31))
        self.comboBoxSection.setObjectName("comboBoxSection")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.comboBoxSection.addItem("")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 230, 1101, 551))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        alternative=[]
        for etudiant in self.ISIMM.Etudiants:
            if(etudiant.section==self.comboBoxSection.currentText() and etudiant.niveauEtude==self.comboBoxNiveau.currentText()):
                alternative.append([etudiant.nInscription,etudiant.nom,etudiant.prenom,etudiant.dateN,etudiant.adresse,etudiant.mail,etudiant.telephone,etudiant.section,etudiant.niveauEtude])

        alternative=[]
        for note in self.ISIMM.Notes:
            if(self.ISIMM.getEtudiant(note.nInscription).section==self.comboBoxSection.currentText() and self.ISIMM.getEtudiant(note.nInscription).niveauEtude==self.comboBoxNiveau.currentText()):
                alternative.append([note.nInscription,self.ISIMM.getEtudiant(note.nInscription).nom,self.ISIMM.getEtudiant(note.nInscription).prenom,note.code,self.ISIMM.getMatiere(note.code).designation,note.noteDS,note.noteEX])
        self.modal=TableModel(alternative)
        
        self.tableView.setModel(self.modal)
        self.horizontal_header = self.tableView.horizontalHeader()
        self.vertical_header = self.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(3)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.comboBoxSection.currentTextChanged.connect(self.comboChanged)
        self.comboBoxNiveau.currentTextChanged.connect(self.comboChanged)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBoxNiveau.setItemText(0, _translate("Dialog", "1"))
        self.comboBoxNiveau.setItemText(1, _translate("Dialog", "2"))
        self.comboBoxNiveau.setItemText(2, _translate("Dialog", "3"))
        self.label_10.setText(_translate("Dialog", "Recherche par Section et Niveau"))
        self.comboBoxSection.setItemText(0, _translate("Dialog", "Cycle preparatoire integre (CPI)"))
        self.comboBoxSection.setItemText(1, _translate("Dialog", "Diplome national d\'ingenieur(ING)"))
        self.comboBoxSection.setItemText(2, _translate("Dialog", "Licence en sciences de l’informatique(L-I)"))
        self.comboBoxSection.setItemText(3, _translate("Dialog", "Licence en mathematiques appliquee (L-M)"))