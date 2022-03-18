
class Etudiant:
    def __init__(self,nInscription,nom,prenom,dateN,adresse,mail,telephone,section,niveauEtude):
        self.nInscription=nInscription
        self.nom=nom
        self.prenom=prenom
        self.dateN=dateN
        self.adresse=adresse
        self.mail=mail
        self.telephone=telephone
        self.section=section
        self.niveauEtude=niveauEtude
    
    def __str__(self):
        return "["+self.nInscription+", "+self.nom+", "+self.prenom+", "+self.dateN.toString()+", "+self.adresse+", "+self.mail+", "+self.telephone+", "+self.section+", "+self.niveauEtude+"]"