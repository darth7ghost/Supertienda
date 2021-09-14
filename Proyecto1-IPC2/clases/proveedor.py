class Proveedor:
    def __init__(self, codProv, nitProv, nomProv, dirProv, telProv, cantFac):
        self.codProv = codProv
        self.nitProv = nitProv
        self.nomProv = nomProv
        self.dirProv = dirProv
        self.telProv = telProv
        self.cantFac = cantFac

    #---Codigo de proveedor---
    def getCodProv(self):
        return self.codProv
    
    def setCodProv(self, codProv):
        self.codProv = codProv

    #---NIT de proveedor---
    def getNitProv(self):
        return self.nitProv
    
    def setNitProv(self, nitProv):
        self.nitProv = nitProv

    #---Nombre de proveedor---
    def getNomProv(self):
        return self.nomProv
    
    def setNomProv(self, nomProv):
        self.nomProv = nomProv 

    #---Dirección de proveedor---
    def getDirProv(self):
        return self.dirProv
    
    def setDirProv(self, dirProv):
        self.dirProv = dirProv 

    #---Teléfono de proveedor---
    def getTelProv(self):
        return self.telProv
    
    def setDirProv(self, telProv):
        self.telProv = telProv

    def getCantFac(self):
        return self.cantFac   

    def __repr__(self):
        return f"Código: {self.codProv}, NIT: {self.nitProv}, Nombre: {self.nomProv}, Dirección: {self.dirProv}, Teléfono: {self.telProv}, Unidades facturadas: {self.cantFac}"