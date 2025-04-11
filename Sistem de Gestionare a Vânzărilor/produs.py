class Produs:
    def __init__(self, id, nume, pret, stoc):
        self.id = id
        self.nume = nume
        self.pret = pret
        self.stoc = stoc
        
    def to_dict(self):
        return {
            "id": self.id,
            "nume": self.nume,
            "pret": self.pret,
            "stoc": self.stoc
        }
        
    def __str__(self):
        return f"{self.nume} (ID: {self.id}) - {self.pret} lei, Stoc: {self.stoc}"
    
    def actualizeaza_stoc(self, cantitate):
        self.stoc += cantitate
        
    def __eq__(self, other):
        if isinstance(other, Produs):
            return self.id == other.id
        return False
