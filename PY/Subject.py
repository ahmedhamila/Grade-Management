
class Matiere:
    def __init__(self,code,designation,section,coefficient,semestre):
        self.code=code
        self.designation=designation
        self.section=section
        self.coefficient=coefficient
        self.semestre=semestre
    def __str__(self):
        return "["+self.code+", "+self.designation+", "+self.section+", "+self.coefficient+", "+self.semestre+"]"