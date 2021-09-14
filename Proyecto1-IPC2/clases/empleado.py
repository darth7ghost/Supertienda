class Empleado:
    def __init__(self, codEmp, nomEmp, tipEmp, cantFac):
        self.codEmp = codEmp
        self.nomEmp = nomEmp
        self.tipEmp = tipEmp
        self.cantFac = cantFac

    def getCodEmp(self):
        return self.codEmp
    
    def setCodEmp(self, codEmp):
        self.codEmp = codEmp

    def getNomEmp(self):
        return self.nomEmp
    
    def setNomEmp(self, nomEmp):
        self.nomEmp = nomEmp

    def getTipEmp(self):
        return self.tipEmp
    
    def setTipEmp(self, tipEmp):
        self.tipEmp = tipEmp

    def getCantFac(self):
        return self.cantFac

    def __repr__(self):
        return f"Código: {self.codEmp}, Nombre: {self.nomEmp}, Tipo: {self.tipEmp}, Facturas: {self.cantFac}"