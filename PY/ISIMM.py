class Institut:
    def __init__(self):
        self.Etudiants=[]
        self.Matieres=[]
        self.Notes=[]
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

    def ajouterNote(self,N):
        self.Notes.append(N)

    def afficherNotes(self):
        for i in self.Notes:
            print(i)
    def getNote(self,code,nInscr):
        for i in self.Notes:
            if(i.code==code and i.nInscription==nInscr):
                return i
        return False
    def moyenne(self,noteDS,noteEX):
        return (float(noteEX)*2+float(noteDS))/3
    def rang(self,e,m):
        es=[]
        for note in self.Notes:
            if note.code==m.code:
                es.append(note)
        for i in range (len(es)):
            max=i
            for j in range(i+1,len(es)):
                if(self.moyenne(j.noteDS,j.noteEX)>self.moyenne(max.noteDS,max.noteEX)):
                    max=j
            if(max!=i):
                sw=max
                max=i
                i=sw
        for i in es :
            if(i.nInscription==e.nInscription):
                return es.index(i)+1
               