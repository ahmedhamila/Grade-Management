from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from AddStudent import Ui_Dialog as add
from DeleteStudent import Ui_Dialog as remove
from EditStudent import Ui_Dialog as edit
from Display import Ui_Dialog as afficher
from SearchStudentNInscr import Ui_Dialog as rechercherNumeroInscription
from SearchStudentSection import Ui_Dialog as rechercherSection
from SearchStudentNiveau import Ui_Dialog as rechercherNiveau
from SearchStudentSectionNiveau import Ui_Dialog as rechercherSectionNiveau
from AddSubject import Ui_Dialog as ajouterMatiere
from DeleteSubject import Ui_Dialog as supprimerMatiere
from EditSubject import Ui_Dialog as modifierMatiere
from DisplaySubject import Ui_Dialog as afficherMatiere
from SearchSubjectCode import Ui_Dialog as rechercherMatiereCode
from SearchSubjectSection import Ui_Dialog as rechercherMatiereSection
from SearchSubjectSectionSemestre import Ui_Dialog as rechercherMatiereSectionSemestre
from AddGrade import Ui_Dialog as ajouterNote
from DeleteGrade import Ui_Dialog as supprimerNote
from EditGrade import Ui_Dialog as modifierNote
from DisplayGrade import Ui_Dialog as afficherNote
from SearchGradeNInscr import Ui_Dialog as rechercherNoteNumeroInscription
from SearchGradeSectionNiveau import Ui_Dialog as rechercherNoteSectionNiveau
from SearchGradeNumeroInscriptionSemestre import Ui_Dialog as rechercherNoteNumeroInscriptionSemestre
from ReportCard import Ui_Dialog as bulletinNoteEtudiant
from ReportCardSemestre import Ui_Dialog as bulletinNoteEtudiantSemestre
from AdmittedStudents import Ui_Dialog as admittedStudents
from FailedStudents import Ui_Dialog as failedStudents
from AdmittedStudentsISIMM import Ui_Dialog as admittedStudentsISIMM
from FailedStudentsISIMM import Ui_Dialog as failedStudentsISIMM
from Student import Etudiant
from Subject import Matiere
from Grade import Note

class Ui_MainWindow(object):
    def ajouterEtudiant(self):
        self.setupStacked(2)
        self.stackedWidget.setCurrentWidget(self.windowAjouter)

    def supprimerEtudiant(self):
        self.setupStacked(3)
        self.stackedWidget.setCurrentWidget(self.windowSupprimer)
    
    def modifierEtudiant(self):
        self.setupStacked(4)
        self.stackedWidget.setCurrentWidget(self.windowModifier)
    def afficherEtudiant(self):
        self.setupStacked(5)
        self.stackedWidget.setCurrentWidget(self.windowAfficher)
    def rechercherNumeroInscription(self):
        self.setupStacked(6)
        self.stackedWidget.setCurrentWidget(self.windowRechercherNumeroInscription)
    def rechercherSection(self):
        self.setupStacked(7)
        self.stackedWidget.setCurrentWidget(self.windowRechercherSection)
    def rechercherNiveau(self):
        self.setupStacked(8)
        self.stackedWidget.setCurrentWidget(self.windowRechercherNiveau)
    def rechercherSectionNiveau(self):
        self.setupStacked(9)
        self.stackedWidget.setCurrentWidget(self.windowRechercherSectionNiveau)
    
    def ajouterMatiere(self):
        self.setupStacked(10)
        self.stackedWidget.setCurrentWidget(self.windowAjouterMatiere)
    def supprimerMatiere(self):
        self.setupStacked(11)
        self.stackedWidget.setCurrentWidget(self.windowSupprimerMatiere)
    def modifierMatiere(self):
        self.setupStacked(12)
        self.stackedWidget.setCurrentWidget(self.windowModifierMatiere)
    def afficherMatiere(self):
        self.setupStacked(13)
        self.stackedWidget.setCurrentWidget(self.windowAfficherMatiere)
    def rechercherMatiereCode(self):
        self.setupStacked(14)
        self.stackedWidget.setCurrentWidget(self.windowRechercherMatiereCode)
    def rechercherMatiereSection(self):
        self.setupStacked(15)
        self.stackedWidget.setCurrentWidget(self.windowRechercherMatiereSection)
    def rechercherMatiereSectionSemestre(self):
        self.setupStacked(16)
        self.stackedWidget.setCurrentWidget(self.windowRechercherMatiereSectionSemestre)
    def ajouterNote(self):
        self.setupStacked(17)
        self.stackedWidget.setCurrentWidget(self.windowAjouterNote)
    def supprimerNote(self):
        self.setupStacked(18)
        self.stackedWidget.setCurrentWidget(self.windowSupprimerNote)
    def modfierNote(self):
        self.setupStacked(19)
        self.stackedWidget.setCurrentWidget(self.windowModifierNote)
    def afficherNote(self):
        self.setupStacked(20)
        self.stackedWidget.setCurrentWidget(self.windowAfficherNote)
    def rechercherNoteNumeroInscription(self):
        self.setupStacked(21)
        self.stackedWidget.setCurrentWidget(self.windowRechercherNoteNumeroInscription)
    def rechercherNoteSectionNiveau(self):
        self.setupStacked(22)
        self.stackedWidget.setCurrentWidget(self.windowRechercherNoteSectionNiveau)
    def rechercherNoteNumeroInscriptionSemestre(self):
        self.setupStacked(23)
        self.stackedWidget.setCurrentWidget(self.windowRechercherNoteNumeroInscriptionSemestre)
    def bulletinNoteEtudiant(self):
        self.setupStacked(24)
        self.stackedWidget.setCurrentWidget(self.windowBulletinNoteEtudiant)
    def bulletinNoteEtudiantSemestre(self):
        self.setupStacked(25)
        self.stackedWidget.setCurrentWidget(self.windowBulletinNoteEtudiantSemestre)
    def admittedStudentsSection(self):
        self.setupStacked(26)
        self.stackedWidget.setCurrentWidget(self.windowAdmittedStudents)
    def failedStudentsSection(self):
        self.setupStacked(27)
        self.stackedWidget.setCurrentWidget(self.windowFailedStudents)
    def admittedStudentsISIMM(self):
        self.setupStacked(28)
        self.stackedWidget.setCurrentWidget(self.windowAdmittedStudentsISIMM)
    def failedStudentsISIMM(self):
        self.setupStacked(29)
        self.stackedWidget.setCurrentWidget(self.windowFailedStudentsISIMM)
    def setupStacked(self,index):
        #index 2
        if(index==2):
            self.windowAjouter=QDialog()
            self.ui1=add(self.ISIMM)
            self.ui1.setupUi(self.windowAjouter)
            self.stackedWidget.addWidget(self.windowAjouter)
        #index 3
        elif(index==3):
            self.windowSupprimer=QDialog()
            self.ui2=remove(self.ISIMM)
            self.ui2.setupUi(self.windowSupprimer)
            self.stackedWidget.addWidget(self.windowSupprimer)
        #index 4
        elif(index==4):
            self.windowModifier=QDialog()
            self.ui3=edit(self.ISIMM)
            self.ui3.setupUi(self.windowModifier)
            self.stackedWidget.addWidget(self.windowModifier)
        #index 5
        elif(index==5):
            self.windowAfficher=QDialog()
            self.ui4=afficher(self.ISIMM)
            self.ui4.setupUi(self.windowAfficher)
            self.stackedWidget.addWidget(self.windowAfficher)
        elif(index==6):
            self.windowRechercherNumeroInscription=QDialog()
            self.ui5=rechercherNumeroInscription(self.ISIMM)
            self.ui5.setupUi(self.windowRechercherNumeroInscription)
            self.stackedWidget.addWidget(self.windowRechercherNumeroInscription)
        elif(index==7):
            self.windowRechercherSection=QDialog()
            self.ui6=rechercherSection(self.ISIMM)
            self.ui6.setupUi(self.windowRechercherSection)
            self.stackedWidget.addWidget(self.windowRechercherSection)
        elif(index==8):
            self.windowRechercherNiveau=QDialog()
            self.ui7=rechercherNiveau(self.ISIMM)
            self.ui7.setupUi(self.windowRechercherNiveau)
            self.stackedWidget.addWidget(self.windowRechercherNiveau)
        elif(index==9):
            self.windowRechercherSectionNiveau=QDialog()
            self.ui8=rechercherSectionNiveau(self.ISIMM)
            self.ui8.setupUi(self.windowRechercherSectionNiveau)
            self.stackedWidget.addWidget(self.windowRechercherSectionNiveau)
        elif(index==10):
            self.windowAjouterMatiere=QDialog()
            self.ui9=ajouterMatiere(self.ISIMM)
            self.ui9.setupUi(self.windowAjouterMatiere)
            self.stackedWidget.addWidget(self.windowAjouterMatiere)
        elif(index==11):
            self.windowSupprimerMatiere=QDialog()
            self.ui10=supprimerMatiere(self.ISIMM)
            self.ui10.setupUi(self.windowSupprimerMatiere)
            self.stackedWidget.addWidget(self.windowSupprimerMatiere)
        elif(index==12):
            self.windowModifierMatiere=QDialog()
            self.ui11=modifierMatiere(self.ISIMM)
            self.ui11.setupUi(self.windowModifierMatiere)
            self.stackedWidget.addWidget(self.windowModifierMatiere)
        elif(index==13):
            self.windowAfficherMatiere=QDialog()
            self.ui12=afficherMatiere(self.ISIMM)
            self.ui12.setupUi(self.windowAfficherMatiere)
            self.stackedWidget.addWidget(self.windowAfficherMatiere)
        elif(index==14):
            self.windowRechercherMatiereCode=QDialog()
            self.ui13=rechercherMatiereCode(self.ISIMM)
            self.ui13.setupUi(self.windowRechercherMatiereCode)
            self.stackedWidget.addWidget(self.windowRechercherMatiereCode)
        elif(index==15):
            self.windowRechercherMatiereSection=QDialog()
            self.ui14=rechercherMatiereSection(self.ISIMM)
            self.ui14.setupUi(self.windowRechercherMatiereSection)
            self.stackedWidget.addWidget(self.windowRechercherMatiereSection)
        elif(index==16):
            self.windowRechercherMatiereSectionSemestre=QDialog()
            self.ui15=rechercherMatiereSectionSemestre(self.ISIMM)
            self.ui15.setupUi(self.windowRechercherMatiereSectionSemestre)
            self.stackedWidget.addWidget(self.windowRechercherMatiereSectionSemestre)
        elif(index==17):
            self.windowAjouterNote=QDialog()
            self.ui16=ajouterNote(self.ISIMM)
            self.ui16.setupUi(self.windowAjouterNote)
            self.stackedWidget.addWidget(self.windowAjouterNote)
        elif(index==18):
            self.windowSupprimerNote=QDialog()
            self.ui17=supprimerNote(self.ISIMM)
            self.ui17.setupUi(self.windowSupprimerNote)
            self.stackedWidget.addWidget(self.windowSupprimerNote)
        elif(index==19):
            self.windowModifierNote=QDialog()
            self.ui18=modifierNote(self.ISIMM)
            self.ui18.setupUi(self.windowModifierNote)
            self.stackedWidget.addWidget(self.windowModifierNote)
        elif(index==20):
            self.windowAfficherNote=QDialog()
            self.ui19=afficherNote(self.ISIMM)
            self.ui19.setupUi(self.windowAfficherNote)
            self.stackedWidget.addWidget(self.windowAfficherNote)
        elif(index==21):
            self.windowRechercherNoteNumeroInscription=QDialog()
            self.ui20=rechercherNoteNumeroInscription(self.ISIMM)
            self.ui20.setupUi(self.windowRechercherNoteNumeroInscription)
            self.stackedWidget.addWidget(self.windowRechercherNoteNumeroInscription)
        elif(index==22):
            self.windowRechercherNoteSectionNiveau=QDialog()
            self.ui21=rechercherNoteSectionNiveau(self.ISIMM)
            self.ui21.setupUi(self.windowRechercherNoteSectionNiveau)
            self.stackedWidget.addWidget(self.windowRechercherNoteSectionNiveau)
        elif(index==23):
            self.windowRechercherNoteNumeroInscriptionSemestre=QDialog()
            self.ui22=rechercherNoteNumeroInscriptionSemestre(self.ISIMM)
            self.ui22.setupUi(self.windowRechercherNoteNumeroInscriptionSemestre)
            self.stackedWidget.addWidget(self.windowRechercherNoteNumeroInscriptionSemestre)
        elif(index==24):
            self.windowBulletinNoteEtudiant=QDialog()
            self.ui23=bulletinNoteEtudiant(self.ISIMM)
            self.ui23.setupUi(self.windowBulletinNoteEtudiant)
            self.stackedWidget.addWidget(self.windowBulletinNoteEtudiant)
        elif(index==25):
            self.windowBulletinNoteEtudiantSemestre=QDialog()
            self.ui24=bulletinNoteEtudiantSemestre(self.ISIMM)
            self.ui24.setupUi(self.windowBulletinNoteEtudiantSemestre)
            self.stackedWidget.addWidget(self.windowBulletinNoteEtudiantSemestre)
        elif(index==26):
            self.windowAdmittedStudents=QDialog()
            self.ui25=admittedStudents(self.ISIMM)
            self.ui25.setupUi(self.windowAdmittedStudents)
            self.stackedWidget.addWidget(self.windowAdmittedStudents)
        elif(index==27):
            self.windowFailedStudents=QDialog()
            self.ui26=failedStudents(self.ISIMM)
            self.ui26.setupUi(self.windowFailedStudents)
            self.stackedWidget.addWidget(self.windowFailedStudents)
        elif(index==28):
            self.windowAdmittedStudentsISIMM=QDialog()
            self.ui27=admittedStudentsISIMM(self.ISIMM)
            self.ui27.setupUi(self.windowAdmittedStudentsISIMM)
            self.stackedWidget.addWidget(self.windowAdmittedStudentsISIMM)
        elif(index==29):
            self.windowFailedStudentsISIMM=QDialog()
            self.ui28=failedStudentsISIMM(self.ISIMM)
            self.ui28.setupUi(self.windowFailedStudentsISIMM)
            self.stackedWidget.addWidget(self.windowFailedStudentsISIMM)
        


    def __init__(self,ISIMM):
        self.ISIMM=ISIMM

    def parseStudent(self,line):
        lis=line.split(",")
        lis[8]=lis[8].replace("\n","")
        return Etudiant(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8])   

    def enregistrerEtudiant(self):
        F=open("./Save/SaveEtudiant.csv","w+")
        F.seek(0)
        F.write("Numero d'inscription,Nom,Prenom,Date de naissance,Adresse,Mail,Telephone,Section,Niveau d'etude\n")
        for i in self.ISIMM.Etudiants:
            found=False
            for j in F:
                numI=j.split(",")[0]
                if(numI==i.nInscription):
                    found=True
                    break
            if(not found):
                F.write(i.nInscription+","+i.nom+","+i.prenom+","+str(i.dateN.year())+"/"+str(i.dateN.month())+"/"+str(i.dateN.day())+","+i.adresse+","+i.mail+","+i.telephone+","+i.section+","+i.niveauEtude+"\n")
                
        F.close()
    def recupererEtudiant(self):
        self.ISIMM.Etudiants.clear()
        F=open("./Save/SaveEtudiant.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.ISIMM.Etudiants.append(self.parseStudent(line))
            
        F.close()
    def parseMatiere(self,line):
        lis=line.split(",")
        lis[4]=lis[4].replace("\n","")
        return Matiere(lis[0],lis[1],lis[2],lis[3],lis[4])
    def enregistrerMatiere(self):
        F=open("./Save/SaveMatiere.csv","w+")
        F.seek(0)
        F.write("Code Matiere,Designation,Section,Coefficient,Semestre\n")
        for i in self.ISIMM.Matieres:
            found=False
            for j in F:
                code=j.split(",")[0]
                if(code==i.code):
                    found=True
                    break
            if(not found):
                F.write(i.code+","+i.designation+","+i.section+","+i.coefficient+","+i.semestre+"\n")
                
        F.close()
    def recupererMatiere(self):
        self.ISIMM.Matieres.clear()
        F=open("./Save/SaveMatiere.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.ISIMM.Matieres.append(self.parseMatiere(line))
            
        F.close()
    def recupererTout(self):
        self.recupererEtudiant()
        self.recupererMatiere()
        self.recupererNote()
    
    def parseNote(self,line):
        lis=line.split(",")
        lis[3]=lis[3].replace("\n","")
        return Note(lis[0],lis[1],lis[2],lis[3])
    def enregistrerNote(self):
        F=open("./Save/SaveNote.csv","w+")
        F.seek(0)
        F.write("Numero d'inscription,Code matiere,Note DS,Note EX\n")
        for i in self.ISIMM.Notes:
            found=False
            for j in F:
                code=j.split(",")[1]
                nInscr=j.split(",")[0]
                if(code==i.code and nInscr==i.nInscription):
                    found=True
                    break
            if(not found):
                F.write(i.nInscription+","+i.code+","+i.noteDS+","+i.noteEX+"\n")
                
        F.close()
    def recupererNote(self):
        self.ISIMM.Notes.clear()
        F=open("./Save/SaveNote.csv","r")
        count=-1
        for line in F:
            count+=1
            if(count==0):
                continue
            self.ISIMM.Notes.append(self.parseNote(line))
        F.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 832)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 75 12pt \"Arial\";background-color:#A09FA0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1121, 821))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 24))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color:#777477;")
        self.menubar.setObjectName("menubar")
        self.menuGestion_des_etudiants = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_etudiants.setGeometry(QtCore.QRect(348, 145, 245, 112))
        self.menuGestion_des_etudiants.setObjectName("menuGestion_des_etudiants")
        self.menuMise_jour_des_tudiants = QtWidgets.QMenu(self.menuGestion_des_etudiants)
        self.menuMise_jour_des_tudiants.setObjectName("menuMise_jour_des_tudiants")
        self.menuRecherche_Affichage_etudiant = QtWidgets.QMenu(self.menuGestion_des_etudiants)
        self.menuRecherche_Affichage_etudiant.setObjectName("menuRecherche_Affichage_etudiant")
        self.menuRechercher_tudiants = QtWidgets.QMenu(self.menuRecherche_Affichage_etudiant)
        self.menuRechercher_tudiants.setObjectName("menuRechercher_tudiants")
        self.menuGestion_des_matieres = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_matieres.setObjectName("menuGestion_des_matieres")
        self.menuMise_jour_des_mati_res = QtWidgets.QMenu(self.menuGestion_des_matieres)
        self.menuMise_jour_des_mati_res.setObjectName("menuMise_jour_des_mati_res")
        self.menuRecherche_Affichage = QtWidgets.QMenu(self.menuGestion_des_matieres)
        self.menuRecherche_Affichage.setObjectName("menuRecherche_Affichage")
        self.menuRechercher_matier_s = QtWidgets.QMenu(self.menuRecherche_Affichage)
        self.menuRechercher_matier_s.setObjectName("menuRechercher_matier_s")
        self.menuGestion_des_notes = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_notes.setObjectName("menuGestion_des_notes")
        self.menuRecherche_Affichage_2 = QtWidgets.QMenu(self.menuGestion_des_notes)
        self.menuRecherche_Affichage_2.setObjectName("menuRecherche_Affichage_2")
        self.menuRechercher_notes = QtWidgets.QMenu(self.menuRecherche_Affichage_2)
        self.menuRechercher_notes.setObjectName("menuRechercher_notes")
        self.menuMise_jour_des_notes = QtWidgets.QMenu(self.menuGestion_des_notes)
        self.menuMise_jour_des_notes.setObjectName("menuMise_jour_des_notes")
        self.menuCalcul_et_affichage = QtWidgets.QMenu(self.menubar)
        self.menuCalcul_et_affichage.setObjectName("menuCalcul_et_affichage")
        self.menuEnregistrement_et_Recuperation = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrement_et_Recuperation.setObjectName("menuEnregistrement_et_Recuperation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAjouter_un_etudiant = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_etudiant.setObjectName("actionAjouter_un_etudiant")
        self.actionSupprimer_un_etudiant = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_etudiant.setObjectName("actionSupprimer_un_etudiant")
        self.actionModifier_un_etudiant = QtWidgets.QAction(MainWindow)
        self.actionModifier_un_etudiant.setObjectName("actionModifier_un_etudiant")
        self.actionAfficher_les_etudiants = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_etudiants.setObjectName("actionAfficher_les_etudiants")
        self.actionAjouter_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_matiere.setObjectName("actionAjouter_une_matiere")
        self.actionSupprimer_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_matiere.setObjectName("actionSupprimer_une_matiere")
        self.actionModifier_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_matiere.setObjectName("actionModifier_une_matiere")
        self.actionAfficher_les_matieres = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_matieres.setObjectName("actionAfficher_les_matieres")
        self.actionAjouter_une_note = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_note.setObjectName("actionAjouter_une_note")
        self.actionSupprimer_une_note = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_note.setObjectName("actionSupprimer_une_note")
        self.actionModifier_une_note = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_note.setObjectName("actionModifier_une_note")
        self.actionAfficher_les_notes = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_notes.setObjectName("actionAfficher_les_notes")
        self.actionBulletin_de_note_d_un_etudiant = QtWidgets.QAction(MainWindow)
        self.actionBulletin_de_note_d_un_etudiant.setObjectName("actionBulletin_de_note_d_un_etudiant")
        self.actionBulletin_de_note_d_un_etudiant_par_semestre = QtWidgets.QAction(MainWindow)
        self.actionBulletin_de_note_d_un_etudiant_par_semestre.setObjectName("actionBulletin_de_note_d_un_etudiant_par_semestre")
        self.actionEtudiants_admis_d_une_section = QtWidgets.QAction(MainWindow)
        self.actionEtudiants_admis_d_une_section.setObjectName("actionEtudiants_admis_d_une_section")
        self.actionEtudiants_redoublants_d_une_section = QtWidgets.QAction(MainWindow)
        self.actionEtudiants_redoublants_d_une_section.setObjectName("actionEtudiants_redoublants_d_une_section")
        self.actionEtudiants_admis_de_l_ISIMM = QtWidgets.QAction(MainWindow)
        self.actionEtudiants_admis_de_l_ISIMM.setObjectName("actionEtudiants_admis_de_l_ISIMM")
        self.actionEtudiants_redoublants_de_l_ISIMM = QtWidgets.QAction(MainWindow)
        self.actionEtudiants_redoublants_de_l_ISIMM.setObjectName("actionEtudiants_redoublants_de_l_ISIMM")
        self.actionMoyennes_des_etudiants_d_une_section = QtWidgets.QAction(MainWindow)
        self.actionMoyennes_des_etudiants_d_une_section.setObjectName("actionMoyennes_des_etudiants_d_une_section")
        self.actionEnregistrement_des_etudiants = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_des_etudiants.setObjectName("actionEnregistrement_des_etudiants")
        self.actionRecuperation_des_etudiants = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_des_etudiants.setObjectName("actionRecuperation_des_etudiants")
        self.actionEnregistrement_des_matieres = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_des_matieres.setObjectName("actionEnregistrement_des_matieres")
        self.actionRecuperation_des_matieres = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_des_matieres.setObjectName("actionRecuperation_des_matieres")
        self.actionEnregistrement_des_notes = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement_des_notes.setObjectName("actionEnregistrement_des_notes")
        self.actionRecuperation_des_matieres_2 = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_des_matieres_2.setObjectName("actionRecuperation_des_matieres_2")
        self.actionRecherche_par_numero_d_inscription = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_numero_d_inscription.setObjectName("actionRecherche_par_numero_d_inscription")
        self.actionRecherche_par_Section = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Section.setObjectName("actionRecherche_par_Section")
        self.actionRecherche_par_Niveau = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Niveau.setObjectName("actionRecherche_par_Niveau")
        self.actionRecherche_par_Section_et_Niveau = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Section_et_Niveau.setObjectName("actionRecherche_par_Section_et_Niveau")
        self.actionRecherche_par_Code = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Code.setObjectName("actionRecherche_par_Code")
        self.actionRecherche_par_Section_2 = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Section_2.setObjectName("actionRecherche_par_Section_2")
        self.actionRecherche_par_Section_et_Semestre = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Section_et_Semestre.setObjectName("actionRecherche_par_Section_et_Semestre")
        self.actionRecherche_par_numero_d_inscription_2 = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_numero_d_inscription_2.setObjectName("actionRecherche_par_numero_d_inscription_2")
        self.actionRecherche_par_Section_et_Niveau_2 = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_Section_et_Niveau_2.setObjectName("actionRecherche_par_Section_et_Niveau_2")
        self.actionRecherche_par_numero_d_inscription_et_Semestre = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_numero_d_inscription_et_Semestre.setObjectName("actionRecherche_par_numero_d_inscription_et_Semestre")
        self.actionRecuperation_de_tout = QtWidgets.QAction(MainWindow)
        self.actionRecuperation_de_tout.setObjectName("actionRecuperation_de_tout")
        self.menuMise_jour_des_tudiants.addAction(self.actionAjouter_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionSupprimer_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionModifier_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuRechercher_tudiants.addAction(self.actionRecherche_par_numero_d_inscription)
        self.menuRechercher_tudiants.addSeparator()
        self.menuRechercher_tudiants.addAction(self.actionRecherche_par_Section)
        self.menuRechercher_tudiants.addSeparator()
        self.menuRechercher_tudiants.addAction(self.actionRecherche_par_Niveau)
        self.menuRechercher_tudiants.addSeparator()
        self.menuRechercher_tudiants.addAction(self.actionRecherche_par_Section_et_Niveau)
        self.menuRechercher_tudiants.addSeparator()
        self.menuRecherche_Affichage_etudiant.addAction(self.actionAfficher_les_etudiants)
        self.menuRecherche_Affichage_etudiant.addSeparator()
        self.menuRecherche_Affichage_etudiant.addAction(self.menuRechercher_tudiants.menuAction())
        self.menuRecherche_Affichage_etudiant.addSeparator()
        self.menuGestion_des_etudiants.addAction(self.menuMise_jour_des_tudiants.menuAction())
        self.menuGestion_des_etudiants.addSeparator()
        self.menuGestion_des_etudiants.addAction(self.menuRecherche_Affichage_etudiant.menuAction())
        self.menuGestion_des_etudiants.addSeparator()
        self.menuMise_jour_des_mati_res.addAction(self.actionAjouter_une_matiere)
        self.menuMise_jour_des_mati_res.addSeparator()
        self.menuMise_jour_des_mati_res.addAction(self.actionSupprimer_une_matiere)
        self.menuMise_jour_des_mati_res.addSeparator()
        self.menuMise_jour_des_mati_res.addAction(self.actionModifier_une_matiere)
        self.menuMise_jour_des_mati_res.addSeparator()
        self.menuRechercher_matier_s.addAction(self.actionRecherche_par_Code)
        self.menuRechercher_matier_s.addSeparator()
        self.menuRechercher_matier_s.addAction(self.actionRecherche_par_Section_2)
        self.menuRechercher_matier_s.addSeparator()
        self.menuRechercher_matier_s.addAction(self.actionRecherche_par_Section_et_Semestre)
        self.menuRechercher_matier_s.addSeparator()
        self.menuRecherche_Affichage.addAction(self.actionAfficher_les_matieres)
        self.menuRecherche_Affichage.addSeparator()
        self.menuRecherche_Affichage.addAction(self.menuRechercher_matier_s.menuAction())
        self.menuRecherche_Affichage.addSeparator()
        self.menuGestion_des_matieres.addAction(self.menuMise_jour_des_mati_res.menuAction())
        self.menuGestion_des_matieres.addSeparator()
        self.menuGestion_des_matieres.addAction(self.menuRecherche_Affichage.menuAction())
        self.menuGestion_des_matieres.addSeparator()
        self.menuRechercher_notes.addAction(self.actionRecherche_par_numero_d_inscription_2)
        self.menuRechercher_notes.addSeparator()
        self.menuRechercher_notes.addAction(self.actionRecherche_par_Section_et_Niveau_2)
        self.menuRechercher_notes.addSeparator()
        self.menuRechercher_notes.addAction(self.actionRecherche_par_numero_d_inscription_et_Semestre)
        self.menuRechercher_notes.addSeparator()
        self.menuRecherche_Affichage_2.addAction(self.actionAfficher_les_notes)
        self.menuRecherche_Affichage_2.addSeparator()
        self.menuRecherche_Affichage_2.addAction(self.menuRechercher_notes.menuAction())
        self.menuRecherche_Affichage_2.addSeparator()
        self.menuMise_jour_des_notes.addAction(self.actionAjouter_une_note)
        self.menuMise_jour_des_notes.addSeparator()
        self.menuMise_jour_des_notes.addAction(self.actionSupprimer_une_note)
        self.menuMise_jour_des_notes.addSeparator()
        self.menuMise_jour_des_notes.addAction(self.actionModifier_une_note)
        self.menuMise_jour_des_notes.addSeparator()
        self.menuGestion_des_notes.addAction(self.menuMise_jour_des_notes.menuAction())
        self.menuGestion_des_notes.addSeparator()
        self.menuGestion_des_notes.addAction(self.menuRecherche_Affichage_2.menuAction())
        self.menuGestion_des_notes.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionBulletin_de_note_d_un_etudiant)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionBulletin_de_note_d_un_etudiant_par_semestre)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionEtudiants_admis_d_une_section)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionEtudiants_redoublants_d_une_section)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionEtudiants_admis_de_l_ISIMM)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuCalcul_et_affichage.addAction(self.actionEtudiants_redoublants_de_l_ISIMM)
        self.menuCalcul_et_affichage.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionEnregistrement_des_etudiants)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionRecuperation_des_etudiants)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionEnregistrement_des_matieres)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionRecuperation_des_matieres)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionEnregistrement_des_notes)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionRecuperation_des_matieres_2)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menuEnregistrement_et_Recuperation.addAction(self.actionRecuperation_de_tout)
        self.menuEnregistrement_et_Recuperation.addSeparator()
        self.menubar.addAction(self.menuGestion_des_etudiants.menuAction())
        self.menubar.addAction(self.menuGestion_des_matieres.menuAction())
        self.menubar.addAction(self.menuGestion_des_notes.menuAction())
        self.menubar.addAction(self.menuCalcul_et_affichage.menuAction())
        self.menubar.addAction(self.menuEnregistrement_et_Recuperation.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionAjouter_un_etudiant.triggered.connect(self.ajouterEtudiant)
        self.actionSupprimer_un_etudiant.triggered.connect(self.supprimerEtudiant)
        self.actionEnregistrement_des_etudiants.triggered.connect(self.enregistrerEtudiant)
        self.actionRecuperation_des_etudiants.triggered.connect(self.recupererEtudiant)
        self.actionModifier_un_etudiant.triggered.connect(self.modifierEtudiant)
        self.actionAfficher_les_etudiants.triggered.connect(self.afficherEtudiant)
        self.actionRecherche_par_numero_d_inscription.triggered.connect(self.rechercherNumeroInscription)
        self.actionRecherche_par_Section.triggered.connect(self.rechercherSection)
        self.actionRecherche_par_Niveau.triggered.connect(self.rechercherNiveau)
        self.actionRecherche_par_Section_et_Niveau.triggered.connect(self.rechercherSectionNiveau)

        self.actionAjouter_une_matiere.triggered.connect(self.ajouterMatiere)
        self.actionSupprimer_une_matiere.triggered.connect(self.supprimerMatiere)
        self.actionModifier_une_matiere.triggered.connect(self.modifierMatiere)
        self.actionAfficher_les_matieres.triggered.connect(self.afficherMatiere)
        self.actionRecherche_par_Code.triggered.connect(self.rechercherMatiereCode)
        self.actionRecherche_par_Section_2.triggered.connect(self.rechercherMatiereSection)
        self.actionRecherche_par_Section_et_Semestre.triggered.connect(self.rechercherMatiereSectionSemestre)
        self.actionEnregistrement_des_matieres.triggered.connect(self.enregistrerMatiere)
        self.actionRecuperation_des_matieres.triggered.connect(self.recupererMatiere)

        self.actionAjouter_une_note.triggered.connect(self.ajouterNote)
        self.actionEnregistrement_des_notes.triggered.connect(self.enregistrerNote)
        self.actionRecuperation_des_matieres_2.triggered.connect(self.recupererNote)
        self.actionSupprimer_une_note.triggered.connect(self.supprimerNote)
        self.actionModifier_une_note.triggered.connect(self.modfierNote)
        self.actionAfficher_les_notes.triggered.connect(self.afficherNote)
        self.actionRecherche_par_numero_d_inscription_2.triggered.connect(self.rechercherNoteNumeroInscription)
        self.actionRecherche_par_Section_et_Niveau_2.triggered.connect(self.rechercherNoteSectionNiveau)
        self.actionRecherche_par_numero_d_inscription_et_Semestre.triggered.connect(self.rechercherNoteNumeroInscriptionSemestre)

        self.actionBulletin_de_note_d_un_etudiant.triggered.connect(self.bulletinNoteEtudiant)
        self.actionBulletin_de_note_d_un_etudiant_par_semestre.triggered.connect(self.bulletinNoteEtudiantSemestre)
        self.actionEtudiants_admis_d_une_section.triggered.connect(self.admittedStudentsSection)
        self.actionEtudiants_redoublants_d_une_section.triggered.connect(self.failedStudentsSection)
        self.actionEtudiants_admis_de_l_ISIMM.triggered.connect(self.admittedStudentsISIMM)
        self.actionEtudiants_redoublants_de_l_ISIMM.triggered.connect(self.failedStudentsISIMM)

        self.actionRecuperation_de_tout.triggered.connect(self.recupererTout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGestion_des_etudiants.setTitle(_translate("MainWindow", "Gestion des étudiants"))
        self.menuMise_jour_des_tudiants.setTitle(_translate("MainWindow", "Mise à jour des étudiants"))
        self.menuRecherche_Affichage_etudiant.setTitle(_translate("MainWindow", "Recherche,Affichage"))
        self.menuRechercher_tudiants.setTitle(_translate("MainWindow", "Rechercher étudiants"))
        self.menuGestion_des_matieres.setTitle(_translate("MainWindow", "Gestion des matières"))
        self.menuMise_jour_des_mati_res.setTitle(_translate("MainWindow", "Mise à jour des matières"))
        self.menuRecherche_Affichage.setTitle(_translate("MainWindow", "Recherche,Affichage"))
        self.menuRechercher_matier_s.setTitle(_translate("MainWindow", "Rechercher matierès"))
        self.menuGestion_des_notes.setTitle(_translate("MainWindow", "Gestion des notes"))
        self.menuRecherche_Affichage_2.setTitle(_translate("MainWindow", "Recherche, Affichage"))
        self.menuRechercher_notes.setTitle(_translate("MainWindow", "Rechercher notes"))
        self.menuMise_jour_des_notes.setTitle(_translate("MainWindow", "Mise à jour des notes"))
        self.menuCalcul_et_affichage.setTitle(_translate("MainWindow", "Calcul et affichage"))
        self.menuEnregistrement_et_Recuperation.setTitle(_translate("MainWindow", "Enregistrement et Récupération"))
        self.actionAjouter_un_etudiant.setText(_translate("MainWindow", "Ajouter un étudiant"))
        self.actionSupprimer_un_etudiant.setText(_translate("MainWindow", "Supprimer un étudiant"))
        self.actionModifier_un_etudiant.setText(_translate("MainWindow", "Modifier un étudiant"))
        self.actionAfficher_les_etudiants.setText(_translate("MainWindow", "Afficher les étudiants"))
        self.actionAjouter_une_matiere.setText(_translate("MainWindow", "Ajouter une mètiere"))
        self.actionSupprimer_une_matiere.setText(_translate("MainWindow", "Supprimer une matière"))
        self.actionModifier_une_matiere.setText(_translate("MainWindow", "Modifier une matière"))
        self.actionAfficher_les_matieres.setText(_translate("MainWindow", "Afficher les matières"))
        self.actionAjouter_une_note.setText(_translate("MainWindow", "Ajouter une note"))
        self.actionSupprimer_une_note.setText(_translate("MainWindow", "Supprimer une note"))
        self.actionModifier_une_note.setText(_translate("MainWindow", "Modifier une note"))
        self.actionAfficher_les_notes.setText(_translate("MainWindow", "Afficher les notes"))
        self.actionBulletin_de_note_d_un_etudiant.setText(_translate("MainWindow", "Bulletin de note d\'un étudiant"))
        self.actionBulletin_de_note_d_un_etudiant_par_semestre.setText(_translate("MainWindow", "Bulletin de note d\'un étudiant par semestre"))
        self.actionEtudiants_admis_d_une_section.setText(_translate("MainWindow", "Etudiants admis d\'une section"))
        self.actionEtudiants_redoublants_d_une_section.setText(_translate("MainWindow", "Etudiants redoublants d\'une section"))
        self.actionEtudiants_admis_de_l_ISIMM.setText(_translate("MainWindow", "Etudiants admis de l\'ISIMM"))
        self.actionEtudiants_redoublants_de_l_ISIMM.setText(_translate("MainWindow", "Etudiants redoublants de l\'ISIMM"))
        self.actionMoyennes_des_etudiants_d_une_section.setText(_translate("MainWindow", "Moyennes des étudiants d\'une section"))
        self.actionEnregistrement_des_etudiants.setText(_translate("MainWindow", "Enregistrement des étudiants"))
        self.actionRecuperation_des_etudiants.setText(_translate("MainWindow", "Récupération des étudiants"))
        self.actionEnregistrement_des_matieres.setText(_translate("MainWindow", "Enregistrement des matières"))
        self.actionRecuperation_des_matieres.setText(_translate("MainWindow", "Récupération des matières"))
        self.actionEnregistrement_des_notes.setText(_translate("MainWindow", "Enregistrement des notes"))
        self.actionRecuperation_des_matieres_2.setText(_translate("MainWindow", "Récupération des notes"))
        self.actionRecherche_par_numero_d_inscription.setText(_translate("MainWindow", "Recherche par numero d\'inscription"))
        self.actionRecherche_par_Section.setText(_translate("MainWindow", "Recherche par Section"))
        self.actionRecherche_par_Niveau.setText(_translate("MainWindow", "Recherche par Niveau"))
        self.actionRecherche_par_Section_et_Niveau.setText(_translate("MainWindow", "Recherche par Section et Niveau"))
        self.actionRecherche_par_Code.setText(_translate("MainWindow", "Recherche par Code"))
        self.actionRecherche_par_Section_2.setText(_translate("MainWindow", "Recherche par Section"))
        self.actionRecherche_par_Section_et_Semestre.setText(_translate("MainWindow", "Recherche par Section et Semestre"))
        self.actionRecherche_par_numero_d_inscription_2.setText(_translate("MainWindow", "Recherche par numero d\'inscription"))
        self.actionRecherche_par_Section_et_Niveau_2.setText(_translate("MainWindow", "Recherche par Section et Niveau"))
        self.actionRecherche_par_numero_d_inscription_et_Semestre.setText(_translate("MainWindow", "Recherche par numero d\'inscription et Semestre"))
        self.actionRecuperation_de_tout.setText(_translate("MainWindow", "Récupération de tout"))
