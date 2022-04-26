from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtPrintSupport
from PyQt5.Qt import QFileInfo
from ReportCardPDF import Ui_Dialog as PDF
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
    def displayPDF(self):
        fn, _ = QFileDialog.getSaveFileName(self.dg, 'Export PDF', None, 'PDF files (.pdf);;All Files()')
        if fn != '':
            if QFileInfo(fn).suffix() == "" : fn += '.pdf'
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            painter = QtGui.QPainter(printer)
            dlg=QDialog()
            self.ui=PDF(self.ISIMM,self.comboBoxEtudiant.currentText().split(" ")[0])
            self.ui.setupUi(dlg)
            xscale = printer.pageRect().width() * 1.0 / dlg.width()
            yscale = printer.pageRect().height() * 1.0 / dlg.height()
            scale = min(xscale, yscale)
            painter.translate(printer.paperRect().center())
            painter.scale(scale, scale*1.2)
            painter.translate(-dlg.width() / 2, -dlg.height() / 2)


            dlg.render(painter)
            painter.end()
    def comboChanged(self):
        self.modal.deleteLater()
        nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
        self.labelAdresse.setText(self.ISIMM.getEtudiant(nInscr).adresse)
        self.labelNomPrenom.setText(self.ISIMM.getEtudiant(nInscr).nom+" "+self.ISIMM.getEtudiant(nInscr).prenom)
        self.labelNomSection.setText(self.ISIMM.getEtudiant(nInscr).section)
        self.labelNomDateN.setText(str(self.ISIMM.getEtudiant(nInscr).dateN.year())+"/"+str(self.ISIMM.getEtudiant(nInscr).dateN.month())+"/"+str(self.ISIMM.getEtudiant(nInscr).dateN.day()))
        alternative=[]
        somme_coeff=0
        somme_moyenne=0
        for note in self.ISIMM.Notes:
            if(note.nInscription==self.comboBoxEtudiant.currentText().split(" ")[0]):
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
    def setupUi(self, Dialog):
        self.dg=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1156, 810)
        Dialog.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(440, 30, 311, 41))
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(830, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(830, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.labelAdresse = QtWidgets.QLabel(Dialog)
        self.labelAdresse.setGeometry(QtCore.QRect(910, 130, 191, 31))
        self.labelAdresse.setText("")
        self.labelAdresse.setObjectName("labelAdresse")
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
        self.labelNomSection = QtWidgets.QLabel(Dialog)
        self.labelNomSection.setGeometry(QtCore.QRect(100, 180, 271, 31))
        self.labelNomSection.setText("")
        self.labelNomSection.setObjectName("labelNomSection")
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
        self.labelNomDateN = QtWidgets.QLabel(Dialog)
        self.labelNomDateN.setGeometry(QtCore.QRect(190, 230, 191, 31))
        self.labelNomDateN.setText("")
        self.labelNomDateN.setObjectName("labelNomDateN")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.comboBoxEtudiant = QtWidgets.QComboBox(Dialog)
        self.comboBoxEtudiant.setGeometry(QtCore.QRect(220, 90, 311, 31))
        self.comboBoxEtudiant.setObjectName("comboBoxEtudiant")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(0, 260, 1161, 481))
        self.tableView.setStyleSheet("text-align:center;")
        self.tableView.setMidLineWidth(2)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 1271, 841))
        self.label_7.setMidLineWidth(2)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Back/Background.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.PDF = QtWidgets.QPushButton(Dialog)
        self.PDF.setGeometry(QtCore.QRect(940, 760, 201, 31))
        self.PDF.setObjectName("PDF")
        self.label_7.raise_()
        self.label_10.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.labelAdresse.raise_()
        self.labelNomPrenom.raise_()
        self.label_3.raise_()
        self.labelNomSection.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.labelNomDateN.raise_()
        self.label_6.raise_()
        self.comboBoxEtudiant.raise_()
        self.tableView.raise_()
        self.PDF.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        for i in self.ISIMM.Etudiants:
            self.comboBoxEtudiant.addItem(i.nInscription+" "+i.nom+" "+i.prenom)

        if len(self.ISIMM.Etudiants)>0 :
            nInscr=self.comboBoxEtudiant.currentText().split(" ")[0]
            self.labelAdresse.setText(self.ISIMM.getEtudiant(nInscr).adresse)
            self.labelNomPrenom.setText(self.ISIMM.getEtudiant(nInscr).nom+" "+self.ISIMM.getEtudiant(nInscr).prenom)
            self.labelNomSection.setText(self.ISIMM.getEtudiant(nInscr).section)
            self.labelNomDateN.setText(str(self.ISIMM.getEtudiant(nInscr).dateN.year())+"/"+str(self.ISIMM.getEtudiant(nInscr).dateN.month())+"/"+str(self.ISIMM.getEtudiant(nInscr).dateN.day()))
            alternative=[]
            somme_coeff=0
            somme_moyenne=0
            for note in self.ISIMM.Notes:
                if(note.nInscription==self.comboBoxEtudiant.currentText().split(" ")[0]):
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
        self.comboBoxEtudiant.currentTextChanged.connect(self.comboChanged)

        self.PDF.clicked.connect(self.displayPDF)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "Bulletin de note"))
        self.label.setText(_translate("Dialog", "Année scolaire 2021/2022"))
        self.label_2.setText(_translate("Dialog", "Adresse:"))
        self.label_3.setText(_translate("Dialog", "Nom et Prénom :"))
        self.label_4.setText(_translate("Dialog", "Section :"))
        self.label_5.setText(_translate("Dialog", "Date de naissance :"))
        self.label_6.setText(_translate("Dialog", "Numero d\'inscription :"))
        self.PDF.setText(_translate("Dialog", "Export AS PDF"))
import Backgrounds
