class Factura:
    def __init__(self, codFac, codEmp, nomEmp, tipEmp, nitClien, nomClien, lstCompra, total, noCaja):
        self.codFac = codFac
        self.codEmp = codEmp
        self.nomEmp = nomEmp
        self.tipEmp = tipEmp
        self.nitClien = nitClien
        self.nomClien = nomClien
        self.lstCompra = lstCompra
        self.total = total
        self.noCaja = noCaja

    def getCodFac(self):
        return self.codFac

    def getCodEmp(self):
        return self.codEmp

    def getNomEmp(self):
        return self.nomEmp

    def getTipEmp(self):
        return self.tipEmp

    def getNitClien(self):
        return self.nitClien

    def getNomClien(self):
        return self.nomClien

    def getLstCompra(self):
        return self.lstCompra

    def getTotal(self):
        return self.total

    def getNoCaja(self):
        return self.noCaja
    
    def __repr__(self):
        return f"Fac. no.: {self.codFac}, Empleado: {self.codEmp}- {self.nomEmp}, Cliente: {self.nitClien} - {self.nomEmp}, Total: Q{self.total}, Compras: "