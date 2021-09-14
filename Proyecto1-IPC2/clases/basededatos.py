import os
import msvcrt
from clases import registro

clsRegistro = registro.Registro

class BD:
    def menuRegistro(self):
        while True:
            op = 0  
            os.system ("cls")
            print("----------------------------------------------")
            print("         Supertienda LA COBANERITA")
            print("           --- BASE DE DATOS ---")
            print("[1].-Registro.\n[2].-Edición.\n[3].-Eliminación.\n[4].-Reportes\n[5].-Buscar facturas\n\n[0].-Regresar.")
            op = int(input("\n->Seleccione la opción que desee: "))
            if op==1:
                os.system ("cls")
                print("----------------------------------------------")
                print("         Supertienda LA COBANERITA")
                print("            --- REGISTRO ---")
                print("[1].-Artículos.\n[2].-Proveedores.\n[3].-Empleados.\n[4].-Clientes.\n\n[0].-Regresar.")
                op = int(input("\n->Seleccione la opción que desee: "))
                if op==1:
                    clsRegistro.registroArticulo(self)
                elif op==2:
                    clsRegistro.registroProveedor(self)
                elif op==3:
                    clsRegistro.registroEmpleado(self)
                elif op==4:
                    clsRegistro.registroCliente(self)
                elif op==0:
                    break
                else:
                    print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                    print("Presione 'Enter' para regresar, e intente nuevamente...")
                    msvcrt.getch()
            elif op==2:
                os.system ("cls")
                print("----------------------------------------------")
                print("         Supertienda LA COBANERITA")
                print("            --- EDICIÓN ---")
                print("[1].-Artículos.\n[2].-Proveedores.\n[3].-Empleados.\n[4].-Clientes.\n\n[0].-Regresar.")
                op = int(input("\n->Seleccione la opción que desee: "))
                if op == 1:
                    clsRegistro.editarArticulo(self)
                elif op == 2:
                    clsRegistro.editarProveedor(self)
                elif op == 3:
                    clsRegistro.editarEmpleado(self)
                elif op == 4:
                    clsRegistro.editarCliente(self)
                elif op == 0:
                    break
                else:
                    print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                    print("Presione 'Enter' para regresar, e intente nuevamente...")
                    msvcrt.getch()
            elif op==3:
                os.system ("cls")
                print("----------------------------------------------")
                print("         Supertienda LA COBANERITA")
                print("            --- ELIMINACIÓN ---")
                print("[1].-Artículos.\n[2].-Proveedores.\n[3].-Empleados.\n[4].-Clientes.\n[5].-Facturas\n\n[0].-Regresar.")
                op = int(input("\n->Seleccione la opción que desee: "))
                if op == 1:
                    clsRegistro.eliminarArticulo(self)
                elif op == 2:
                    clsRegistro.eliminarProveedor(self)
                elif op == 3:
                    clsRegistro.eliminarEmpleado(self)
                elif op == 4:
                    clsRegistro.eliminarCliente(self)
                elif op == 5:
                    clsRegistro.eliminarFactura(self)
                elif op == 0:
                    break
                else:
                    print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                    print("Presione 'Enter' para regresar, e intente nuevamente...")
                    msvcrt.getch()
            elif op==4:
                os.system ("cls")
                print("----------------------------------------------")
                print("         Supertienda LA COBANERITA")
                print("            --- REPORTES ---")
                print("[1].-Artículos.\n[2].-Proveedores.\n[3].-Empleados.\n[4].-Clientes.\n[5].-Facturas.\n\n[0].-Regresar.")
                op = int(input("\n->Seleccione la opción que desee: "))
                if op == 1:
                    clsRegistro.reporteArticulo(self)
                elif op == 2:
                    clsRegistro.reporteProveedor(self)
                elif op == 3:
                    clsRegistro.reporteEmpleado(self)
                elif op == 4:
                    clsRegistro.reporteCliente(self)
                elif op == 5:
                    os.system ("cls")
                    print("----------------------------------------------")
                    print("         Supertienda LA COBANERITA")
                    print("            --- REPORTES ---")
                    print("[1].-Facturas totales.\n[2].-Facturas por cliente.\n\n[0].-Regresar.")
                    op = int(input("\n->Seleccione la opción que desee: "))
                    if op == 1:
                        clsRegistro.reporteFactura(self)
                    elif op == 2:
                        clsRegistro.reporteFacturaCliente(self)
                    elif op == 0:
                        break
                    else:
                        print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                        print("Presione 'Enter' para regresar, e intente nuevamente...")
                        msvcrt.getch()
                elif op == 0:
                    break
                else:
                    print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                    print("Presione 'Enter' para regresar, e intente nuevamente...")
                    msvcrt.getch()
            elif op==5:
                clsRegistro.buscarFactura(self)
            elif op==0:
                break
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
                msvcrt.getch()
                continue