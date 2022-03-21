
class Note:
    def __init__(self,nInscription,code,noteDS,noteEX):
        self.nInscription=nInscription
        self.code=code
        self.noteDS=noteDS
        self.noteEX=noteEX
    def __str__(self):
        return "["+self.nInscription+", "+self.code+", "+self.noteDS+", "+self.noteEX+"]"
