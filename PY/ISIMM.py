class Institut:
    def __init__(self):
        self.Etudiants=[]
        self.Matieres=[]
    def ajouterEtudiant(self,E):
        self.Etudiants.append(E)

    def afficherEtudiants(self):
        for i in self.Etudiants:
            print(i)
    def getEtudiant(self,nInscr):
        for i in self.Etudiants:
            if(i.nInscription==nInscr):
                return i
        return False
    def ajouterMatiere(self,M):
        self.Matieres.append(M)

    def afficherMatieres(self):
        for i in self.Matieres:
            print(i)
    def getMatiere(self,code):
        for i in self.Matieres:
            if(i.code==code):
                return i
        return False
    