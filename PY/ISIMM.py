class Institut:
    def __init__(self):
        self.Etudiants=[]
    
    def ajouterEtudiant(self,E):
        self.Etudiants.append(E)

    def afficherEtudiants(self):
        for i in self.Etudiants:
            print(i)