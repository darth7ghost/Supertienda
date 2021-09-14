class Cliente:
    def __init__(self, nitClien, nomClien, dirClien, cantCompra, cantFac):
        self.nitClien = nitClien
        self.nomClien = nomClien
        self.dirClien = dirClien
        self.cantCompra = cantCompra
        self.cantFac = cantFac

    def getNitClien(self):
        return self.nitClien

    def setNitClien(self, nitClien):
        self.nitClien = nitClien

    def getNomClien(self):
        return self.nomClien

    def setNomClien(self, nomClien):
        self.nomClien = nomClien

    def getDirClien(self):
        return self.dirClien

    def setDirClien(self, dirClien):
        self.dirClien = dirClien

    def getCantCompra(self):
        return self.cantCompra
    
    def getCantFac(self):
        return self.cantFac

    def __repr__(self):
        return f"NIT: {self.nitClien}, Nombre: {self.nomClien}, Dirección: {self.dirClien}, Total comprado: {self.cantCompra} artículos, Facturas: {self.cantFac}"