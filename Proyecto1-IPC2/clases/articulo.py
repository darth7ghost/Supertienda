class Articulo:
    def __init__(self, codArt, codProvArt, nomArt, cantArt, precArt, cantCompra):
        self.codArt = codArt
        self.codProvArt = codProvArt
        self.nomArt = nomArt
        self.cantArt = cantArt
        self.precArt = precArt
        self.cantCompra = cantCompra

    def getCodArt(self):
        return self.codArt

    def setCodArt(self, codArt):
        self.codArt = codArt

    def getCodProvArt(self):
        return self.codArt

    def setCodProvArt(self, codProvArt):
        self.codProvArt = codProvArt

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
        self.precArt = precArt

    def getCantCompra(self):
        return self.cantCompra  

    def __repr__(self):
        return f"Código: {self.codArt}, Código de proveedor: {self.codProvArt}, Nombre: {self.nomArt}, Cantidad disponible: {self.cantArt} unidades, Precio unitario: Q.{self.precArt}, Cant. compra: {self.cantCompra}"