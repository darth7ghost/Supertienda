class ArticuloF:
    def __init__(self, codArt, nomArt, cantArt, precArt):
        self.codArt = codArt
        self.nomArt = nomArt
        self.cantArt = cantArt
        self.precArt = precArt

    def getCodArt(self):
        return self.codArt

    def setCodArt(self, codArt):
        self.codArt = codArt

    def getNomArt(self):
        return self.nomArt

    def setNomArt(self, nomArt):
        self.nomArt = nomArt

    def getCantArt(self):
        return self.cantArt

    def setCantArt(self, cantArt):
        self.cantArt = cantArt

    def getPrecArt(self):
        return self.precArt

    def setPrecArt(self, precArt):
        self.precArt = precArt\

    def __repr__(self):
        return f"[{self.codArt}]- {self.nomArt} - {self.cantArt} unidades - Q.{self.precArt}"