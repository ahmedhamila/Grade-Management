from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from AddStudent import Ui_Dialog as add
from DeleteStudent import Ui_Dialog as remove


class Ui_MainWindow(object):
    def ajouterEtudiant(self):
        
        self.stackedWidget.setCurrentIndex(2)

    def supprimerEtudiant(self):
        
        self.stackedWidget.setCurrentIndex(3)

    def setupStacked(self):
        #index 2
        self.windowAjouter=QDialog()
        self.ui1=add(self.ISIMM)
        self.ui1.setupUi(self.windowAjouter)
        self.stackedWidget.addWidget(self.windowAjouter)
        #index 3
        self.windowSupprimer=QDialog()
        self.ui2=remove(self.ISIMM)
        self.ui2.setupUi(self.windowSupprimer)
        self.stackedWidget.addWidget(self.windowSupprimer)


    def __init__(self,ISIMM):
        self.ISIMM=ISIMM
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 850)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 24))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("background-color:#777477;")
        self.menubar.setObjectName("menubar")
        self.menuGestion_des_etudiants = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_etudiants.setGeometry(QtCore.QRect(269, 140, 245, 112))
        self.menuGestion_des_etudiants.setObjectName("menuGestion_des_etudiants")
        self.menuMise_jour_des_tudiants = QtWidgets.QMenu(self.menuGestion_des_etudiants)
        self.menuMise_jour_des_tudiants.setObjectName("menuMise_jour_des_tudiants")
        self.menuRecherche_Affichage_etudiant = QtWidgets.QMenu(self.menuGestion_des_etudiants)
        self.menuRecherche_Affichage_etudiant.setObjectName("menuRecherche_Affichage_etudiant")
        self.menuGestion_des_matieres = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_matieres.setObjectName("menuGestion_des_matieres")
        self.menuMise_jour_des_mati_res = QtWidgets.QMenu(self.menuGestion_des_matieres)
        self.menuMise_jour_des_mati_res.setObjectName("menuMise_jour_des_mati_res")
        self.menuRecherche_Affichage = QtWidgets.QMenu(self.menuGestion_des_matieres)
        self.menuRecherche_Affichage.setObjectName("menuRecherche_Affichage")
        self.menuGestion_des_notes = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_notes.setObjectName("menuGestion_des_notes")
        self.menuRecherche_Affichage_2 = QtWidgets.QMenu(self.menuGestion_des_notes)
        self.menuRecherche_Affichage_2.setObjectName("menuRecherche_Affichage_2")
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
        self.actionRechercher_etudiants = QtWidgets.QAction(MainWindow)
        self.actionRechercher_etudiants.setObjectName("actionRechercher_etudiants")
        self.actionAjouter_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_matiere.setObjectName("actionAjouter_une_matiere")
        self.actionSupprimer_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_matiere.setObjectName("actionSupprimer_une_matiere")
        self.actionModifier_une_matiere = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_matiere.setObjectName("actionModifier_une_matiere")
        self.actionAfficher_les_matieres = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_matieres.setObjectName("actionAfficher_les_matieres")
        self.actionRechercher_matieres = QtWidgets.QAction(MainWindow)
        self.actionRechercher_matieres.setObjectName("actionRechercher_matieres")
        self.actionAjouter_une_note = QtWidgets.QAction(MainWindow)
        self.actionAjouter_une_note.setObjectName("actionAjouter_une_note")
        self.actionSupprimer_une_note = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_une_note.setObjectName("actionSupprimer_une_note")
        self.actionModifier_une_note = QtWidgets.QAction(MainWindow)
        self.actionModifier_une_note.setObjectName("actionModifier_une_note")
        self.actionAfficher_les_notes = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_notes.setObjectName("actionAfficher_les_notes")
        self.actionRechercher_notes = QtWidgets.QAction(MainWindow)
        self.actionRechercher_notes.setObjectName("actionRechercher_notes")
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
        self.menuMise_jour_des_tudiants.addAction(self.actionAjouter_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionSupprimer_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionModifier_un_etudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuRecherche_Affichage_etudiant.addAction(self.actionAfficher_les_etudiants)
        self.menuRecherche_Affichage_etudiant.addSeparator()
        self.menuRecherche_Affichage_etudiant.addAction(self.actionRechercher_etudiants)
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
        self.menuRecherche_Affichage.addAction(self.actionAfficher_les_matieres)
        self.menuRecherche_Affichage.addSeparator()
        self.menuRecherche_Affichage.addAction(self.actionRechercher_matieres)
        self.menuRecherche_Affichage.addSeparator()
        self.menuGestion_des_matieres.addAction(self.menuMise_jour_des_mati_res.menuAction())
        self.menuGestion_des_matieres.addSeparator()
        self.menuGestion_des_matieres.addAction(self.menuRecherche_Affichage.menuAction())
        self.menuGestion_des_matieres.addSeparator()
        self.menuRecherche_Affichage_2.addAction(self.actionAfficher_les_notes)
        self.menuRecherche_Affichage_2.addSeparator()
        self.menuRecherche_Affichage_2.addAction(self.actionRechercher_notes)
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
        self.menuCalcul_et_affichage.addAction(self.actionMoyennes_des_etudiants_d_une_section)
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
        self.menubar.addAction(self.menuGestion_des_etudiants.menuAction())
        self.menubar.addAction(self.menuGestion_des_matieres.menuAction())
        self.menubar.addAction(self.menuGestion_des_notes.menuAction())
        self.menubar.addAction(self.menuCalcul_et_affichage.menuAction())
        self.menubar.addAction(self.menuEnregistrement_et_Recuperation.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setupStacked()
        self.actionAjouter_un_etudiant.triggered.connect(self.ajouterEtudiant)
        self.actionSupprimer_un_etudiant.triggered.connect(self.supprimerEtudiant)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGestion_des_etudiants.setTitle(_translate("MainWindow", "Gestion des étudiants"))
        self.menuMise_jour_des_tudiants.setTitle(_translate("MainWindow", "Mise à jour des étudiants"))
        self.menuRecherche_Affichage_etudiant.setTitle(_translate("MainWindow", "Recherche,Affichage"))
        self.menuGestion_des_matieres.setTitle(_translate("MainWindow", "Gestion des matières"))
        self.menuMise_jour_des_mati_res.setTitle(_translate("MainWindow", "Mise à jour des matières"))
        self.menuRecherche_Affichage.setTitle(_translate("MainWindow", "Recherche,Affichage"))
        self.menuGestion_des_notes.setTitle(_translate("MainWindow", "Gestion des notes"))
        self.menuRecherche_Affichage_2.setTitle(_translate("MainWindow", "Recherche, Affichage"))
        self.menuMise_jour_des_notes.setTitle(_translate("MainWindow", "Mise à jour des notes"))
        self.menuCalcul_et_affichage.setTitle(_translate("MainWindow", "Calcul et affichage"))
        self.menuEnregistrement_et_Recuperation.setTitle(_translate("MainWindow", "Enregistrement et Récupération"))
        self.actionAjouter_un_etudiant.setText(_translate("MainWindow", "Ajouter un étudiant"))
        self.actionSupprimer_un_etudiant.setText(_translate("MainWindow", "Supprimer un étudiant"))
        self.actionModifier_un_etudiant.setText(_translate("MainWindow", "Modifier un étudiant"))
        self.actionAfficher_les_etudiants.setText(_translate("MainWindow", "Afficher les étudiants"))
        self.actionRechercher_etudiants.setText(_translate("MainWindow", "Rechercher étudiants"))
        self.actionAjouter_une_matiere.setText(_translate("MainWindow", "Ajouter une mètiere"))
        self.actionSupprimer_une_matiere.setText(_translate("MainWindow", "Supprimer une matière"))
        self.actionModifier_une_matiere.setText(_translate("MainWindow", "Modifier une matière"))
        self.actionAfficher_les_matieres.setText(_translate("MainWindow", "Afficher les matières"))
        self.actionRechercher_matieres.setText(_translate("MainWindow", "Rechercher matierès"))
        self.actionAjouter_une_note.setText(_translate("MainWindow", "Ajouter une note"))
        self.actionSupprimer_une_note.setText(_translate("MainWindow", "Supprimer une note"))
        self.actionModifier_une_note.setText(_translate("MainWindow", "Modifier une note"))
        self.actionAfficher_les_notes.setText(_translate("MainWindow", "Afficher les notes"))
        self.actionRechercher_notes.setText(_translate("MainWindow", "Rechercher notes"))
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
        self.actionRecuperation_des_matieres_2.setText(_translate("MainWindow", "Récupération des étudiants"))
