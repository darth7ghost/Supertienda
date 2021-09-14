#---Importe de clases---
import msvcrt
import os
import pickle
import clases.proveedor as registroP
import clases.empleado as registroE
import clases.cliente as registroC
import clases.articulo as registroA
import clases.factura as registroF
import clases.articuloF as registroAF

#---Lista para proveedor---
lstProveedor = []

#---Lista para artículo---
lstArticulo = []

#---Lista para cliente---
lstCliente = []

#---Lista para empleado---
lstEmpleado = []

#---Lista para facturas---
lstFactura = []

class Registro():
    #------------------------------ARTICULOS------------------------------
    #---AREGAR ARTICULOS AL SISTEMA---
    def registroArticulo(self):
        #---Cargando proveedores---
        global lstProveedor
        os.system("cls")
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        #---Cargando articulos---
        global lstArticulo
        archivoArticulo = open("articulo.pkl", "ab+")
        archivoArticulo.seek(0)
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print(f"[INFO]-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("[ADVERTENCIA]-No existen artículos registados.")
        finally:
            archivoArticulo.close()
        rep = False
        rep2 = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("   --- REGISTRO DE NUEVOS ARTÍCULOS ---")
        while True:
            try:
                codArt = int(input("Ingrese el código del artículo: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for articulos in lstArticulo:
            if(articulos.getCodArt() == codArt):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            print(f"\n[ADVERTENCIA]-Ya existe un artículo registrado con ese código:")
            articulo = lstArticulo[cnt]
            print(articulo)
            print("\nPresione 'Enter' para regresar, e intente nuevamente...")
        else:
            while True:
                try:
                    codProvArt = int(input("Ingrese el código de proveedor: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            #---Validación de algún código repetido.
            cntProv = 0
            for proveedores in lstProveedor:
                if(proveedores.getCodProv() == codProvArt):
                    nitProv = proveedores.getNitProv()
                    nomProv = proveedores.getNomProv()
                    dirProv = proveedores.getDirProv()
                    telProv = proveedores.getTelProv()
                    cantFac = proveedores.getCantFac()
                    rep2 = True
                    break
                cntProv += 1
            #---Si existe un número repetido.
            if rep2 == True:
                nomArt = input("Ingrese el nombre del artículo: ")
                while True:
                    try:
                        cantArt = int(input("Ingrese la cantidad disponible para el artículo: "))
                    except ValueError:
                        print("[ADVERTENCIA]-La cantidad debe ser un NUMERO.\n")
                        continue
                    else:
                        break
                while True:
                    try:
                        precArt = float(input("Ingrese el costo por unidad: Q."))
                    except ValueError:
                        print("[ADVERTENCIA]-El costo debe ser un NUMERO o DECIMAL.\n")
                        continue
                    else:
                        break
                #---Agregando el nuevo artículo al archivo.
                cantCompra = 0
                lstArticulo.append(registroA.Articulo(codArt, codProvArt, nomArt, cantArt, precArt, cantCompra))
                archivoArticulo = open("articulo.pkl", "wb")
                pickle.dump(lstArticulo, archivoArticulo)
                archivoArticulo.close()
                #---Agregando la cantidad de artículos facturados al proveedor.
                proveedor = lstProveedor[cntProv]
                nCantFac = cantFac + cantArt
                lstProveedor.remove(proveedor)
                lstProveedor.append(registroP.Proveedor(codProvArt, nitProv, nomProv, dirProv, telProv, nCantFac))
                archivoProveedor = open("proveedor.pkl", "wb")
                pickle.dump(lstProveedor, archivoProveedor)
                archivoProveedor.close()
                print("\n[INFO]-El registro del nuevo artículo se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-No existe ningún proveedor con ese código.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---ELIMINAR ARTICULOS DEL SISTEMA.---
    def eliminarArticulo(self):
        os.system("cls")
        global lstArticulo
        archivoArticulo = open("articulo.pkl", "ab+")
        archivoArticulo.seek(0)
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print(f"[INFO]-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("[ADVERTENCIA]-No existen artículos registados.")
        finally:
            archivoArticulo.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("      --- ELIMINACIÓN DE ARTÍCULOS ---")
        while True:
            try:
                codArt = int(input("Ingrese el código del artículo: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for articulos in lstArticulo:
            if(articulos.getCodArt() == codArt):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            articulo = lstArticulo[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea eliminar el artículo [{articulo}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                lstArticulo.remove(articulo)
                archivoArticulo = open("articulo.pkl", "wb")
                pickle.dump(lstArticulo, archivoArticulo)
                archivoArticulo.close()
                print("\n[INFO]-La eliminación del artículo se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            elif opcion ==2:
                print(f"\n[INFO]-Eliminación cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe Ningún artículo registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---EDITAR ARTICULOS DEL SISTEMA.---
    def editarArticulo(self):
        os.system("cls")
        global lstArticulo
        archivoArticulo = open("articulo.pkl", "ab+")
        archivoArticulo.seek(0)
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print(f"[INFO]-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("[ADVERTENCIA]-No existen artículos registados.")
        finally:
            archivoArticulo.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("        --- EDICIÓN DE ARTÍCULOS ---")
        while True:
            try:
                codArt = int(input("Ingrese el código del artículo: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for articulos in lstArticulo:
            if(articulos.getCodArt() == codArt):
                cantCompra = articulos.getCantCompra()
                codProvArt = articulos.getCodProvArt()
                cantArt = articulos.getCantArt()
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            articulo = lstArticulo[cnt]
            cntProv = 0
            for proveedores in lstProveedor:
                if(proveedores.getCodProv() == codProvArt):
                    nitProv = proveedores.getNitProv()
                    nomProv = proveedores.getNomProv()
                    dirProv = proveedores.getDirProv()
                    telProv = proveedores.getTelProv()
                    cantFac = proveedores.getCantFac()
                    rep2 = True
                    break
                cntProv += 1
            if rep2 == True:
                while True:
                    try:
                        opcion = int(input(f"¿Desea editar el artículo [{articulo}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                    except ValueError:
                        print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                        continue
                    else:
                        break
                if opcion == 1:
                    nomArt = input("Ingrese el nombre del artículo: ")
                    while True:
                        try:
                            nCantArt = int(input("Ingrese la cantidad disponible para el artículo: "))
                        except ValueError:
                            print("[ADVERTENCIA]-La cantidad debe ser un NUMERO.\n")
                            continue
                        else:
                            break
                    while True:
                        try:
                            precArt = float(input("Ingrese el costo por unidad: Q."))
                        except ValueError:
                            print("[ADVERTENCIA]-El costo debe ser un NUMERO o un DECIMAL.\n")
                            continue
                        else:
                            break
                    #---Editando el artículo con los nuevos datos.
                    lstArticulo.remove(articulo)
                    lstArticulo.append(registroA.Articulo(codArt, codProvArt, nomArt, nCantArt, precArt, cantCompra))
                    archivoArticulo = open("articulo.pkl", "wb")
                    pickle.dump(lstArticulo, archivoArticulo)
                    archivoArticulo.close()
                    #---Agregando la nueva cantidad al proveedor
                    proveedor = lstProveedor[cntProv]
                    cantAux = nCantArt - cantArt
                    nCantFac = cantFac + cantAux
                    lstProveedor.remove(proveedor)
                    lstProveedor.append(registroP.Proveedor(codProvArt, nitProv, nomProv, dirProv, telProv, nCantFac))
                    archivoProveedor = open("proveedor.pkl", "wb")
                    pickle.dump(lstProveedor, archivoProveedor)
                    archivoProveedor.close()
                    print("\n[INFO]-La edición del artículo se ha realizado correctamente.")
                    print("Presione 'Enter' para regresar...")
                elif opcion ==2:
                    print(f"\n[INFO]-Edición cancelada.")
                    print("Presione 'Enter' para regresar...")
                else:
                    print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                    print("Presione 'Enter' para regresar, e intente nuevamente...")
            else:
                print(f"\n[ADVERTENCIA]-El proveedor relacionado a ese artículo fue eliminado.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe ningún artículo registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()
        
    #------------------------------PROVEEDORES------------------------------
    #---AREGAR PROVEEDORES AL SISTEMA---
    def registroProveedor(self):
        global lstProveedor
        os.system("cls")
        #---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("   --- REGISTRO DE NUEVOS PROVEEDORES ---")
        while True:
            try:
                codProv = int(input("Código del proveedor: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for proveedores in lstProveedor:
            if(proveedores.getCodProv() == codProv):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            print(f"\n[ADVERTENCIA]-Ya existe un proveedor registrado con ese código:")
            proveedor = lstProveedor[cnt]
            print(proveedor)
            print("\nPresione 'Enter' para regresar, e intente nuevamente...")
        else:
            while True:
                try:
                    nitProv = int(input("NIT del proveedor: "))
                except ValueError:
                    print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            nomProv = input("Nombre del proveedor: ")
            direcProv = input("Dirección del proveedor: ")
            telProv = input("No. teléfono del proveedor: ") 
            #---Almacenamiento del nuevo proveedor.---
            cantFac = 0
            lstProveedor.append(registroP.Proveedor(codProv, nitProv, nomProv, direcProv, telProv, cantFac))
            archivoProveedor = open("proveedor.pkl", "wb")
            pickle.dump(lstProveedor, archivoProveedor)
            archivoProveedor.close()
            print("\n[INFO]-El registro del nuevo proveedor se ha realizado correctamente. ---")
            print("Presione 'Enter' para regresar...")
        msvcrt.getch()

    #---ELIMINAR PROVEEDORES DEL SISTEMA.---
    def eliminarProveedor(self):
        global lstProveedor
        os.system("cls")
        #---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("     --- ELIMINACIÓN DE PROVEEDORES ---")
        while True:
            try:
                codProv = int(input("Código del proveedor: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for proveedores in lstProveedor:
            if(proveedores.getCodProv() == codProv):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            proveedor = lstProveedor[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea eliminar al proveedor [{proveedor}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                lstProveedor.remove(proveedor)
                archivoProveedor = open("proveedor.pkl", "wb")
                pickle.dump(lstProveedor, archivoProveedor)
                archivoProveedor.close()
                print("\n[INFO]-La eliminación del proveedor se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Eliminación cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe ningún proveedor registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---EDITAR PROVEEDORES DEL SISTEMA.---
    def editarProveedor(self):
        global lstProveedor
        os.system("cls")
        #---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("       --- EDICIÓN DE PROVEEDORES ---")
        while True:
            try:
                codProv = int(input("Código del proveedor: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for proveedores in lstProveedor:
            if(proveedores.getCodProv() == codProv):
                cantFac = proveedores.getCantFac()
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            proveedor = lstProveedor[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea editar al proveedor [{proveedor}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                while True:
                    try:
                        nitProv = int(input("NIT del proveedor: "))
                    except ValueError:
                        print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                        continue
                    else:
                        break
                nomProv = input("Nombre del proveedor: ")
                direcProv = input("Dirección del proveedor: ")
                telProv = input("No. teléfono del proveedor: ") 
                lstProveedor.remove(proveedor)
                lstProveedor.append(registroP.Proveedor(codProv, nitProv, nomProv, direcProv, telProv, cantFac))
                archivoProveedor = open("proveedor.pkl", "wb")
                pickle.dump(lstProveedor, archivoProveedor)
                archivoProveedor.close()
                print("\n[INFO]-La edición del proveedor se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Edición cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe ningún proveedor registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #------------------------------CLIENTES------------------------------
    #---AREGAR CLIENTES AL SISTEMA---
    def registroCliente(self):
        global lstCliente
        os.system("cls")
        #---Importar datos de clientes a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("    --- REGISTRO DE NUEVOS CLIENTES ---")
        while True:
            try:
                nitClien = int(input("NIT del cliente: "))
            except ValueError:
                print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for clientes in lstCliente:
            if(clientes.getNitClien() == nitClien):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            print(f"\n[ADVERTENCIA]-Ya existe un cliente registrado con ese NIT.")
            cliente = lstCliente[cnt]
            print(cliente)
            print("\nPresione 'Enter' para regresar, e intente nuevamente...")
        else:
            nomClien = input("Nombre del cliente: ")
            dirClien = input("Dirección del cliente: ")
            #---Almacenamiento del nuevo cliente.---
            cantCompra = 0
            cantFac = 0
            lstCliente.append(registroC.Cliente(nitClien, nomClien, dirClien, cantCompra, cantFac))
            archivoCliente = open("cliente.pkl", "wb")
            pickle.dump(lstCliente, archivoCliente)
            archivoCliente.close()
            print("\n[INFO]-El registro del nuevo cliente se ha realizado correctamente.")
            print("Presione 'Enter' para regresar...")
        msvcrt.getch()

    #---ELIMINAR CLIENTES DEL SISTEMA.---
    def eliminarCliente(self):
        global lstCliente
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("       --- ELIMINACIÓN DE CLIENTES ---")
        while True:
            try:
                nitClien = int(input("NIT del cliente: "))
            except ValueError:
                print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for clientes in lstCliente:
            if(clientes.getNitClien() == nitClien):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            cliente = lstCliente[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea eliminar al cliente [{cliente}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                #---Eliminación del nuevo empleado.---
                lstCliente.remove(cliente)
                archivoCliente = open("cliente.pkl", "wb")
                pickle.dump(lstCliente, archivoCliente)
                archivoCliente.close()
                print("\n[INFO]-La eliminación del cliente se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Eliminación cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe ningún cliente registrado con ese NIT.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---EDITAR CLIENTES DEL SISTEMA.---
    def editarCliente(self):
        global lstCliente
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("       --- ELIMINACIÓN DE CLIENTES ---")
        while True:
            try:
                nitClien = int(input("NIT del cliente: "))
            except ValueError:
                print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for clientes in lstCliente:
            if(clientes.getNitClien() == nitClien):
                cantCompra = clientes.getCantCompra()
                cantFac = clientes.getCantFac()
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            cliente = lstCliente[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea editar al cliente [{cliente}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                nomClien = input("Nombre del cliente: ")
                dirClien = input("Dirección del cliente: ")
                lstCliente.remove(cliente)
                lstCliente.append(registroC.Cliente(nitClien, nomClien, dirClien, cantCompra, cantFac))
                archivoCliente = open("cliente.pkl", "wb")
                pickle.dump(lstCliente, archivoCliente)
                archivoCliente.close()
                print("\n[INFO]-La edición del cliente se ha realizado correctamente.")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Edición cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[ADVERTENCIA]-No existe ningún cliente registrado con ese NIT.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #------------------------------EMPLEADOS------------------------------
    #---AREGAR EMPLEADOS AL SISTEMA---
    def registroEmpleado(self):
        global lstEmpleado
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoEmpleado = open("empleado.pkl", "ab+")
        archivoEmpleado.seek(0)
        try:
            lstEmpleado = pickle.load(archivoEmpleado)
            print(f"[INFO]-Se cargaron {len(lstEmpleado)} empleados.")
        except EOFError:
            print("[ADVERTENCIA]-No existen empleados registados.")
        finally:
            archivoEmpleado.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("    --- REGISTRO DE NUEVOS EMPLEADOS ---")
        while True:
            try:
                codEmp = int(input("Código del empleado: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for empleados in lstEmpleado:
            if(empleados.getCodEmp() == codEmp):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            print(f"\n[ADVERTENCIA]-Ya existe un empleado registrado con ese código.")
            emp = lstEmpleado[cnt]
            print(emp)
            print("\nPresione 'Enter' para regresar, e intente nuevamente...")
        else:
            nomEmp = input("Nombre del empelado: ")
            print("TIPOS DE EMPLEADO:\n[1].-Vendedor\n[2].-Cajero\n[3].-Despachador")
            while True:
                try:
                    tipo = int(input("Escriba el tipo de empleado a ser: "))
                except ValueError:
                    print("[ADVERTENCIA]-El tipo debe ser un NUMERO.\n")
                    continue
                else:
                    break
            if tipo == 1:
                tipEmp = "Vendedor"
            elif tipo == 2:
                tipEmp = "Cajero"
            elif tipo == 3:
                tipEmp = "Despachador"
            cantFac = 0
            lstEmpleado.append(registroE.Empleado(codEmp, nomEmp, tipEmp, cantFac))
            archivoEmpleado = open("empleado.pkl", "wb")
            pickle.dump(lstEmpleado, archivoEmpleado)
            archivoEmpleado.close()
            print("\n[INFO]-El registro del nuevo empleado se ha realizado correctamente.")
            print("Presione 'Enter' para regresar...")
        msvcrt.getch()

    #---ELIMINAR EMPLEADOS DEL SISTEMA.---
    def eliminarEmpleado(self):
        global lstEmpleado
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoEmpleado = open("empleado.pkl", "ab+")
        archivoEmpleado.seek(0)
        try:
            lstEmpleado = pickle.load(archivoEmpleado)
            print(f"[INFO]-Se cargaron {len(lstEmpleado)} empleados.")
        except EOFError:
            print("[ADVERTENCIA]-No existen empleados registados.")
        finally:
            archivoEmpleado.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("      --- ELIMINACIÓN DE EMPLEADOS ---")
        while True:
            try:
                codEmp = int(input("Código del empleado: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for empleados in lstEmpleado:
            if(empleados.getCodEmp() == codEmp):
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            empleado = lstEmpleado[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea eliminar al empleado [{empleado}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                #---Eliminación del nuevo empleado.---
                lstEmpleado.remove(empleado)
                archivoEmpleado = open("empleado.pkl", "wb")
                pickle.dump(lstEmpleado, archivoEmpleado)
                archivoEmpleado.close()
                print("\n[INFO]-El empleado se ha eliminado correctamente. ---")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Eliminación cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[INFO]-No existe ningún empleado registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---EDICIÓN DE EMPLEADOS DEL SISTEMA.---
    def editarEmpleado(self):
        global lstEmpleado
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoEmpleado = open("empleado.pkl", "ab+")
        archivoEmpleado.seek(0)
        try:
            lstEmpleado = pickle.load(archivoEmpleado)
            print(f"[INFO]-Se cargaron {len(lstEmpleado)} empleados.")
        except EOFError:
            print("[ADVERTENCIA]-No existen empleados registados.")
        finally:
            archivoEmpleado.close()
        rep = False
        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("        --- EDICIÓN DE EMPLEADOS ---")
        while True:
            try:
                codEmp = int(input("Código del empleado: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido.
        cnt = 0
        for empleados in lstEmpleado:
            if(empleados.getCodEmp() == codEmp):
                cantFac = empleados.getCantFac()
                rep = True
                break
            cnt += 1
        #---Si existe un número repetido.
        if rep == True:
            empleado = lstEmpleado[cnt]
            while True:
                try:
                    opcion = int(input(f"¿Desea editar al empleado [{empleado}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                nomEmp = input("Nombre del empelado: ")
                print("TIPOS DE EMPLEADO:\n[1].-Vendedor\n[2].-Cajero\n[3].-Despachador")
                while True:
                    try:
                        tipo = int(input("Escriba el tipo de empleado a ser: "))
                    except ValueError:
                        print("[ADVERTENCIA]-El tipo debe ser un NUMERO.\n")
                        continue
                    else:
                        break
                if tipo == 1:
                    tipEmp = "Vendedor"
                elif tipo == 2:
                    tipEmp = "Cajero"
                elif tipo == 3:
                    tipEmp = "Despachador"
                lstEmpleado.remove(empleado)
                lstEmpleado.append(registroE.Empleado(codEmp, nomEmp, tipEmp, cantFac))
                archivoEmpleado = open("empleado.pkl", "wb")
                pickle.dump(lstEmpleado, archivoEmpleado)
                archivoEmpleado.close()
                print("\n[INFO]-El empleado se ha editado correctamente. ---")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Edición cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[INFO]-No existe ningún empleado registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #------------------------------FACTURACIÓN------------------------------
    def facturacion(self):
        #---Lista de elementos.---
        lstCompra = []
        lstTotal = []
        inFac = False
        #---Carga de todos los empleados.---
        global lstEmpleado
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoEmpleado = open("empleado.pkl", "ab+")
        archivoEmpleado.seek(0)
        try:
            lstEmpleado = pickle.load(archivoEmpleado)
            print(f"[INFO]-Se cargaron {len(lstEmpleado)} empleados.")
            inFac = True
        except EOFError:
            print("[ADVERTENCIA]-No existen empleados registados.")
            inFac = False
        finally:
            archivoEmpleado.close()
        repEmp = False

        #---Carga de todos los clientes.---  
        global lstCliente
        #---Importar datos de clientes a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        repClien = False

        #---Carga de todas las facturas.---  
        global lstFactura
        #---Importar datos de facturas a la lista.---
        archivoFactura = open("factura.pkl", "ab+")
        archivoFactura.seek(0)
        try:
            lstFactura = pickle.load(archivoFactura)
            print(f"[INFO]-Se cargaron {len(lstFactura)} facturas.")
        except EOFError:
            print("[ADVERTENCIA]-No existen facturas registadas.")
        finally:
            archivoFactura.close()
        repFac = False

        #---Cargando articulos---
        global lstArticulo
        #---Importar datos de artículos a la lista.---
        archivoArticulo = open("articulo.pkl", "ab+")
        archivoArticulo.seek(0)
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print(f"[INFO]-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("[ADVERTENCIA]-No existen artículos registados.")
        finally:
            archivoArticulo.close()
        repArt = False

        #---Cargando proveedores.---
        global lstProveedor
        #---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()

        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("            --- FACTURACIÓN ---")
        #---Solicitar el código del empleado.
        while True:
            try:
                codEmp = int(input("Código del empleado: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Solicitar el número de caja.
        while True:
            try:
                noCaja = int(input("Número de caja: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Validación de algún código repetido de empleados.
        cntEmp = 0
        for empleados in lstEmpleado:
            if(empleados.getCodEmp() == codEmp):
                nomEmp = empleados.getNomEmp()
                tipEmp = empleados.getTipEmp()
                cantFacEmpleado = empleados.getCantFac()
                repEmp = True
                break
            cntEmp += 1
        #---Si existe un empleado.
        if repEmp == True:
            empleado = lstEmpleado[cntEmp]
            print(f"\n\t¡Bienvenido {nomEmp}!")
            while True:
                try:
                    nitClien = int(input("NIT del cliente: "))
                except ValueError:
                    print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            #---Validación de algún código repetido de clientes.
            cntClien = 0
            for clientes in lstCliente:
                if(clientes.getNitClien() == nitClien):
                    nomClien = clientes.getNomClien()
                    dirClien = clientes.getDirClien()
                    cantCompraCliente = clientes.getCantCompra()
                    cantFacCliente = clientes.getCantFac()
                    repClien = True
                    break
                cntClien += 1
            #---Si existe un cliente.
            if repClien == True:
                cliente = lstCliente[cntClien]
                print(f"Datos del cliente: {cliente}")
                if inFac == False:
                    codFac = 1
                else:
                    codFac = len(lstFactura)+1
                while True:
                    #---Agregar artículos a la factura.
                    op = int(input(f"\n¿Desea agregar un artículo?\n[1].- Sí\n[2].- No\nConfirmación: "))
                    if op == 1:

                        #---Cargando articulos---
                        archivoArticulo = open("articulo.pkl", "ab+")
                        archivoArticulo.seek(0)
                        try:
                            lstArticulo = pickle.load(archivoArticulo)
                        except EOFError:
                            print("[ADVERTENCIA]-No existen artículos registados.")
                        finally:
                            archivoArticulo.close()
                        repArt = False
                        #---Solicitar el código de artículo (sustituyendo códigos de barras).
                        while True:
                            try:
                                codArt = int(input("Ingrese el código del artículo: "))
                            except ValueError:
                                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                                continue
                            else:
                                break

                        #---Validación de algún código repetido de artículos.
                        cntArt = 0
                        for articulos in lstArticulo:
                            if(articulos.getCodArt() == codArt):
                                codProvArt = articulos.getCodProvArt()
                                nomArt = articulos.getNomArt()
                                cantArt = articulos.getCantArt()
                                precArt = articulos.getPrecArt()
                                cantCompraArticulo = articulos.getCantCompra()
                                repArt = True
                                break
                            cntArt += 1

                        #---Si se encontró el artículo.
                        if repArt == True:

                            #---En caso no haya stock disponible.
                            if cantArt == 0:
                                print("[ADVERTENCIA]-No hay stock disponible para ese artículo.")
                                print("Presione 'ENTER' para ingresar otro artículo.")
                                msvcrt.getch()
                            else:
                                #---Mostrando datos de artículo y solicitando cantidad.
                                print(f'{nomArt} - Q.{precArt}')
                                total = 0
                                while True:
                                    try:
                                        cant = int(input("Ingrese la cantidad del producto: "))
                                    except ValueError:
                                        print("[ADVERTENCIA]-La cantidad debe contener NUMEROS en su totalidad.\n")
                                        continue
                                    else:
                                        break

                                #---Si la cantidad indicada supera la cantidad disponible.
                                if cant > cantArt:
                                    print("[ADVERTENCIA]-La cantidad excede el stock disponible. Añadiremos la cantidad disponible a la factura.")
                                    #---Manejo de nuevos datos para el articulo.
                                    nCantArt = 0
                                    nCantCompraArticulo = cantCompraArticulo + cantArt
                                    articulo = lstArticulo[cntArt]
                                    lstArticulo.remove(articulo)
                                    lstArticulo.append(registroA.Articulo(codArt, codProvArt, nomArt, nCantArt, precArt, nCantCompraArticulo))
                                    archivoArticulo = open("articulo.pkl", "wb")
                                    pickle.dump(lstArticulo, archivoArticulo)
                                    archivoArticulo.close()
                                    precTotal = precArt*cantArt

                                    #---Manejo de nuevos datos para la lista de compras.
                                    lstTotal.append(precTotal)
                                    lstCompra.append(registroAF.ArticuloF(codArt, nomArt, cantArt, precArt))

                                    #---Solicitar datos de compra del cliente.
                                    cntClien = 0
                                    for clientes in lstCliente:
                                        if(clientes.getNitClien() == nitClien):
                                            nomClien = clientes.getNomClien()
                                            dirClien = clientes.getDirClien()
                                            cantCompraCliente = clientes.getCantCompra()
                                            cantFacCliente = clientes.getCantFac()
                                            repClien = True
                                            break
                                        cntClien += 1

                                    #---Agregar la cantidad de compra al cliente 
                                    nCantCompraCliente = cantCompraCliente + cantArt
                                    cliente = lstCliente[cntClien]
                                    lstCliente.remove(cliente)
                                    lstCliente.append(registroC.Cliente(nitClien, nomClien, dirClien, nCantCompraCliente, cantFacCliente))
                                    archivoCliente = open("cliente.pkl", "wb")
                                    pickle.dump(lstCliente, archivoCliente)
                                    archivoCliente.close()

                                #---Si se ingresa una cantidad válida.
                                else:

                                    #---Manejo de nuevos datos para el articulo.
                                    articulo = lstArticulo[cntArt]
                                    nCantArt = cantArt-cant
                                    nCantCompraArticulo = cantCompraArticulo + cant
                                    precTotal = precArt*cant
                                    lstArticulo.remove(articulo)
                                    lstArticulo.append(registroA.Articulo(codArt, codProvArt, nomArt, nCantArt, precArt, nCantCompraArticulo))
                                    archivoArticulo = open("articulo.pkl", "wb")
                                    pickle.dump(lstArticulo, archivoArticulo)
                                    archivoArticulo.close()

                                    #---Manejo de nuevos datos para la lista de compras.
                                    lstTotal.append(precTotal)
                                    lstCompra.append(registroAF.ArticuloF(codArt, nomArt, cant, precArt))

                                    #---Solicitar datos de compra del cliente.
                                    cntClien = 0
                                    for clientes in lstCliente:
                                        if(clientes.getNitClien() == nitClien):
                                            nomClien = clientes.getNomClien()
                                            dirClien = clientes.getDirClien()
                                            cantCompraCliente = clientes.getCantCompra()
                                            cantFacCliente = clientes.getCantFac()
                                            repClien = True
                                            break
                                        cntClien += 1

                                    #---Agregar la cantidad de compra al cliente.
                                    nCantCompraCliente = cantCompraCliente + cant
                                    cliente = lstCliente[cntClien]
                                    lstCliente.remove(cliente)
                                    lstCliente.append(registroC.Cliente(nitClien, nomClien, dirClien, nCantCompraCliente, cantFacCliente))
                                    archivoCliente = open("cliente.pkl", "wb")
                                    pickle.dump(lstCliente, archivoCliente)
                                    archivoCliente.close()

                    #---Si el cliente ya no desea continuar con la compra de artículos.
                    elif op == 2:
                        break
                    else:
                        print("[INFO]-Seleccione una opción válida.")
                        msvcrt.getch()
                        continue

                #---Impresión en pantalla de la información de factura.
                print("----------------------------------------------")
                print("         Supertienda LA COBANERITA")
                print("          --- FACTURA EMITIDA ---")
                print(f"Cliente:")
                print(cliente)
                print(f"Código de factura: {codFac}")
                print("----------------------------------------------")
                for compras in lstCompra:
                    print(compras)
                for totales in lstTotal:
                    total += totales
                print(f"\nTotal: Q.{total}")
                print("Factura emitida por:")
                print(empleado)

                #---Creacion de la nueva factura.
                lstFactura.append(registroF.Factura(codFac, codEmp, nomEmp, tipEmp, nitClien, nomClien, lstCompra, total, noCaja))
                archivoFactura = open("factura.pkl", "wb")
                pickle.dump(lstFactura, archivoFactura)
                archivoFactura.close()

                #---Solicitar datos de compra del cliente.
                cntClien = 0
                for clientes in lstCliente:
                    if(clientes.getNitClien() == nitClien):
                        nomClien = clientes.getNomClien()
                        dirClien = clientes.getDirClien()
                        cantCompraCliente = clientes.getCantCompra()
                        cantFacCliente = clientes.getCantFac()
                        repClien = True
                        break
                    cntClien += 1

                #---Agregar la nueva factura al cliente.
                nCantFacCliente = cantFacCliente + 1
                nCantCompraCliente = cantCompraCliente + cant
                cliente = lstCliente[cntClien]
                lstCliente.remove(cliente)
                lstCliente.append(registroC.Cliente(nitClien, nomClien, dirClien, nCantCompraCliente, nCantFacCliente))
                archivoCliente = open("cliente.pkl", "wb")
                pickle.dump(lstCliente, archivoCliente)
                archivoCliente.close()

                #---Añadir la nueva factura al empleado.
                nCantFacEmpleado = cantFacEmpleado + 1
                lstEmpleado.remove(empleado)
                lstEmpleado.append(registroE.Empleado(codEmp, nomEmp, tipEmp, nCantFacEmpleado))
                archivoEmpleado = open("empleado.pkl", "wb")
                pickle.dump(lstEmpleado, archivoEmpleado)
                archivoEmpleado.close()
                print("\n[INFO]-Factura emitida exitosamente.")
                print("Presione 'Enter' para regresar...")

            else:
                print(f"\n[INFO]-No existe ningún cliente registrado con ese NIT.")
                print("Presione 'Enter' para ingresar a la pantalla de registro de cliente e inténtelo nuevamente")
                msvcrt.getch()
                Registro.registroCliente(self)
                Registro.facturacion(self)
                
        else:
            print(f"\n[INFO]-No existe ningún empleado registrado con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---BUSQUEDA DE FACTURAS
    def buscarFactura(self):
        os.system("cls")
        #---Carga de todas las facturas.---  
        global lstFactura
        #---Importar datos de facturas a la lista.---
        archivoFactura = open("factura.pkl", "ab+")
        archivoFactura.seek(0)
        try:
            lstFactura = pickle.load(archivoFactura)
            print(f"[INFO]-Se cargaron {len(lstFactura)} facturas.")
        except EOFError:
            print("[ADVERTENCIA]-No existen facturas registadas.")
        finally:
            archivoFactura.close()
        repFac = False

        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("             --- FACTURAS ---")
        #---Solicitar el código del empleado.
        while True:
            try:
                codFac = int(input("Código de factura: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Búsqueda de facturas y almacenamiento de sus datos.
        cntFac = 0
        for facturas in lstFactura:
            if(facturas.getCodFac() == codFac):
                nitClien = facturas.getNitClien()
                nomClien = facturas.getNomClien()
                lstCompras = facturas.getLstCompra()
                total = facturas.getTotal()
                codEmp = facturas.getCodEmp()
                nomEmp = facturas.getNomEmp()
                tipEmp = facturas.getTipEmp()
                noCaja = facturas.getNoCaja()
                repFac = True
                break
            cntFac += 1

        if repFac == True:
            print("___________________________________________________________")
            print('\tSupertienda "LA COBANERITA"')
            print(f'Factura no. {codFac}')
            print(f'Cliente: {nitClien}- {nomClien}')
            print(f'___Lista de compra:')
            for compras in lstCompras:
                print(compras)
            print(f'________Total: Q.{total}')
            print(f'Empleado encargad: {codEmp}- {nomEmp}, {tipEmp}')
            print(f'No. caja: {noCaja}')
            print("\nPresione 'Enter' para regresar...")
        else:
            print(f"\n[INFO]-No existe ninguna factura registrada con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #---ELIMINACIÓN DE FACTURAS---
    def eliminarFactura(self):
        os.system("cls")
        #---Carga de todas las facturas.---  
        global lstFactura
        #---Importar datos de facturas a la lista.---
        archivoFactura = open("factura.pkl", "ab+")
        archivoFactura.seek(0)
        try:
            lstFactura = pickle.load(archivoFactura)
            print(f"[INFO]-Se cargaron {len(lstFactura)} facturas.")
        except EOFError:
            print("[ADVERTENCIA]-No existen facturas registadas.")
        finally:
            archivoFactura.close()
        repFac = False

        print("----------------------------------------------")
        print("         Supertienda LA COBANERITA")
        print("      --- ELIMINACIÓN DE FACTURAS ---")
        #---Solicitar el código del empleado.
        while True:
            try:
                codFac = int(input("Código de factura: "))
            except ValueError:
                print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        #---Búsqueda de facturas y almacenamiento de sus datos.
        cntFac = 0
        for facturas in lstFactura:
            if(facturas.getCodFac() == codFac):
                repFac = True
                break
            cntFac += 1

        if repFac == True:
            factura = lstFactura[cntFac]
            while True:
                try:
                    opcion = int(input(f"¿Desea eliminar la factura [{codFac}]?\n[1].- Sí\n[2].- No\nConfirmación: "))
                except ValueError:
                    print("[ADVERTENCIA]-El código debe contener NUMEROS en su totalidad.\n")
                    continue
                else:
                    break
            if opcion == 1:
                #---Eliminación de la factura.---
                lstFactura.remove(factura)
                archivoFactura = open("factura.pkl", "wb")
                pickle.dump(lstFactura, archivoFactura)
                archivoFactura.close()
                print("\n[INFO]-La factura se ha eliminado correctamente. ---")
                print("Presione 'Enter' para regresar...")
            elif opcion == 2:
                print(f"\n[INFO]-Eliminación cancelada.")
                print("Presione 'Enter' para regresar...")
            else:
                print(f"\n[ADVERTENCIA]-Seleccione una opción válida.")
                print("Presione 'Enter' para regresar, e intente nuevamente...")
        else:
            print(f"\n[INFO]-No existe ninguna factura registrada con ese código.")
            print("Presione 'Enter' para regresar, e intente nuevamente...")
        msvcrt.getch()

    #------------------------------REPORTES------------------------------
    #---REPORTE DE ARTICULOS---
    def reporteArticulo(self):
        os.system("cls")
        global lstArticulo
        archivoArticulo = open("articulo.pkl", "ab+")
        archivoArticulo.seek(0)
        #---Cargando todos los articulos.---
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print(f"[INFO]-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("[ADVERTENCIA]-No existen artículos registados.")
        finally:
            archivoArticulo.close()
        #---Abriendo el archivo .html para su escritura.---
        try:
            print("\n[INFO]-Reporte HTML actualizado.")
            ra = open("reporteArticulo.html", "w")
            ra.write('<html><head><title>Reporte de Artículos</title></head>')
            ra.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Artículos "Supertienda LA COBANERITA"</h2>')
            ra.write('<h3 style="margin-left:60px">Total artículos:</h3>')
            ra.write(f'<p style="margin-left:80px">{len(lstArticulo)} artículos registrados en la tienda.</p>')
            ra.write('<h3 style="margin-left:60px">Artículo que más se vende:</h3>')
            max = None
            for maxArt in lstArticulo:
                if max == None:
                    max = maxArt.getCantCompra()
                    codArt = maxArt.getCodArt()
                    nomArt = maxArt.getNomArt()
                else:
                    if maxArt.getCantCompra()>max:
                        max = maxArt.getCantCompra()
                        codArt = maxArt.getCodArt()
                        nomArt = maxArt.getNomArt()
            ra.write(f'<ul style="margin-left:80px">')
            ra.write(f'<li>Código: {codArt}</li><li>Artículo: {nomArt}</li><li>Unidades vendidas: {max}</li>')
            ra.write(f'</ul>')
            ra.write('<p style="text-align:center">__________________________________________________________________________________________</P>')
            ra.write('<h3 style="margin-left:60px">Listado total de artículos:</h3>')
            ra.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;"><tbody>')
            ra.write('<tr><th>Cod. Art.</th><th>Cod. Prov.</th><th>Artículo</th><th>Cantidad</th><th>Precio</th><th>No. Compras</th></tr>')
            if lstArticulo:
                for articulos in lstArticulo:
                    ra.write('<tr>')
                    ra.write(f'<td>{articulos.getCodArt()}</td>')
                    ra.write(f'<td>{articulos.getCodProvArt()}</td>')
                    ra.write(f'<td>{articulos.getNomArt()}</td>')
                    ra.write(f'<td>{articulos.getCantArt()}</td>')
                    ra.write(f'<td>Q.{articulos.getPrecArt()}</td>')
                    ra.write(f'<td>{articulos.getCantCompra()}</td>')
                    ra.write('</tr>')
            else:
                ra.write('<p style="text-align:center">Aún no existen artículos registrados...</p>')
            ra.write('</tbody></table></body></html>')
        except EOFError:
            print("[ERROR]-No ha sido posible cargar el archivo.")
        finally:
            ra.close()
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()

    #---REPORTE DE PROVEEDORES---
    def reporteProveedor(self):
        global lstProveedor
        os.system("cls")
        #---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"[INFO]-Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("[ADVERTENCIA]-No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        try:
            print("\n[INFO]-Reporte HTML actualizado.")
            rp = open("reporteProveedor.html", "w")
            rp.write("<html><head><title>Reporte de Proveedores</title></head>")
            rp.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Proveedores "Supertienda LA COBANERITA"</h2>')
            rp.write('<h3 style="margin-left:60px">Total proveedores:</h3>')
            rp.write(f'<p style="margin-left:80px">{len(lstProveedor)} proveedores registrados en la tienda.</p>')
            rp.write('<h3 style="margin-left:60px">Proveedor que más factura a tienda:</h3>')
            max = None
            for maxProv in lstProveedor:
                if max == None:
                    max = maxProv.getCantFac()
                    codProv = maxProv.getCodProv()
                    nomProv = maxProv.getNomProv()
                else:
                    if maxProv.getCantFac()>max:
                        max = maxProv.getCantFac()
                        codProv = maxProv.getCodProv()
                        nomProv = maxProv.getNomProv()
            rp.write(f'<ul style="margin-left:80px">')
            rp.write(f'<li>Código: {codProv}</li><li>Nombre: {nomProv}</li><li>Unidades facturadas: {max}</li>')
            rp.write(f'</ul>')
            rp.write('<p style="text-align:center">__________________________________________________________________________________________</p>')
            rp.write('<h3 style="margin-left:60px">Listado total de proveedores:</h3>')
            rp.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;"><tbody>')
            rp.write('<tr><th>Cod. Prov.</th><th>NIT</th><th>Proveedor</th><th>Dirección</th><th>Teléfono</th><th>Art. facturados</th></tr>')
            if lstProveedor:
                for proveedores in lstProveedor:
                    rp.write('<tr>')
                    rp.write(f'<td>{proveedores.getCodProv()}</td>')
                    rp.write(f'<td>{proveedores.getNitProv()}</td>')
                    rp.write(f'<td>{proveedores.getNomProv()}</td>')
                    rp.write(f'<td>{proveedores.getDirProv()}</td>')
                    rp.write(f'<td>{proveedores.getTelProv()}</td>')
                    rp.write(f'<td>{proveedores.getCantFac()}</td>')
                    rp.write('</tr>')
            else:
                rp.write('<p style="text-align:center">Aún no existen proveedores registrados...</p>')
            rp.write('</tbody></table></body></html>')
        except EOFError:
            print("[ERROR]-No ha sido posible cargar el archivo.")
        finally:
            rp.close()
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()

    #---REPORTE DE CLIENTES---
    def reporteCliente(self):
        global lstCliente
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        try:
            print("\n[INFO]-Reporte HTML actualizado.")
            rc = open("reporteCliente.html", "w")
            rc.write("<html><head><title>Reporte de Clientes</title></head>")
            rc.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Clientes "Supertienda LA COBANERITA"</h2>')
            rc.write('<h3 style="margin-left:60px">Total artículos:</h3>')
            rc.write(f'<p style="margin-left:80px">{len(lstCliente)} clientes registrados en la tienda.</p>')
            rc.write('<h3 style="margin-left:60px">Cliente que más compra:</h3>')
            max = None
            for maxClien in lstCliente:
                if max == None:
                    max = maxClien.getCantCompra()
                    codClien = maxClien.getNitClien()
                    nomClien = maxClien.getNomClien()
                else:
                    if maxClien.getCantCompra()>max:
                        max = maxClien.getCantCompra()
                        codClien = maxClien.getNitClien()
                        nomClien = maxClien.getNomClien()
            rc.write(f'<ul style="margin-left:80px">')
            rc.write(f'<li>NIT: {codClien}</li><li>Cliente: {nomClien}</li><li>Artículos comprados: {max}</li>')
            rc.write(f'</ul>')
            rc.write('<p style="text-align:center">__________________________________________________________________________________________</p>')
            rc.write('<h3 style="margin-left:60px">Listado total de clientes:</h3>')
            rc.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;"><tbody>')
            rc.write('<tr><th>NIT</th><th>Nombre</th><th>Dirección</th><th>Art. comprados</th><th>Fac. recibidas</th></tr>')
            if lstCliente:
                for clientes in lstCliente:
                    rc.write('<tr>')
                    rc.write(f'<td>{clientes.getNitClien()}</td>')
                    rc.write(f'<td>{clientes.getNomClien()}</td>')
                    rc.write(f'<td>{clientes.getDirClien()}</td>')
                    rc.write(f'<td>{clientes.getCantCompra()}</td>')
                    rc.write(f'<td>{clientes.getCantFac()}</td>')
                    rc.write('</tr>')
            else:
                rc.write('<p style="text-align:center">Aún no existen clientes registrados...</p>')
            rc.write('</tbody></table></body></html>')
        except EOFError:
            print("[ERROR]-No ha sido posible cargar el archivo.")
        finally:
            rc.close()
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()

    #---REPORTE DE EMPLEADOS---
    def reporteEmpleado(self):
        global lstEmpleado
        os.system("cls")
        #---Importar datos de empleados a la lista.---
        archivoEmpleado = open("empleado.pkl", "ab+")
        archivoEmpleado.seek(0)
        try:
            lstEmpleado = pickle.load(archivoEmpleado)
            print(f"[INFO]-Se cargaron {len(lstEmpleado)} empleados.")
        except EOFError:
            print("[ADVERTENCIA]-No existen empleados registados.")
        finally:
            archivoEmpleado.close()

        try:
            print("\n[INFO]-Reporte HTML actualizado.")
            re = open("reporteEmpleado.html", "w")
            re.write("<html><head><title>Reporte de Empleados</title></head>")
            re.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Empleados "Supertienda LA COBANERITA"</h2>')
            re.write('<h3 style="margin-left:60px">Total empleados:</h3>')
            re.write(f'<p style="margin-left:80px">{len(lstEmpleado)} empleados registrados en la tienda.</p>')
            re.write('<h3 style="margin-left:60px">Empleado que más factura:</h3>')
            max = None
            for maxEmp in lstEmpleado:
                if max == None:
                    max = maxEmp.getCantFac()
                    codEmp = maxEmp.getCodEmp()
                    nomEmp = maxEmp.getNomEmp()
                else:
                    if maxEmp.getCantFac()>max:
                        max = maxEmp.getCantFac()
                        codEmp = maxEmp.getCodEmp()
                        nomEmp = maxEmp.getNomEmp()
            re.write('<ul style="margin-left:80px">')
            re.write(f'<li>Código: {codEmp}</li><li>Empleado: {nomEmp}</li><li>Facturas emitidas: {max}</li>')
            re.write('</ul>')
            re.write('<p style="text-align:center">__________________________________________________________________________________________</p>')
            re.write('<h3 style="margin-left:60px">Listado total de empleados:</h3>')
            re.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;"><tbody>')
            re.write('<tr><th>Código</th><th>Nombre</th><th>Tipo</th><th>Fac. emitidas</th></tr>')
            if lstEmpleado:
                for empleados in lstEmpleado:
                    re.write('<tr>')
                    re.write(f'<td>{empleados.getCodEmp()}</td>')
                    re.write(f'<td>{empleados.getNomEmp()}</td>')
                    re.write(f'<td>{empleados.getTipEmp()}</td>')
                    re.write(f'<td>{empleados.getCantFac()}</td>')
                    re.write('</tr>')
            else:
                re.write('<p style="text-align:center">Aún no existen empleados registrados...</p>')
            re.write('</body></html>')
        except EOFError:
            print("[ERROR]-No ha sido posible cargar el archivo.")
        finally:
            re.close()
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()

    #---REPORTE DE FACTURAS---
    def reporteFactura(self):
        global lstFactura
        os.system("cls")
        #---Importar datos de facturas a la lista.---
        archivoFactura = open("factura.pkl", "ab+")
        archivoFactura.seek(0)
        try:
            lstFactura = pickle.load(archivoFactura)
            print(f"[INFO]-Se cargaron {len(lstFactura)} facturas.")
        except EOFError:
            print("[ADVERTENCIA]-No existen facturas registadas.")
        finally:
            archivoFactura.close()
        try:
            print("\n[INFO]-Reporte HTML actualizado.")
            rf = open("reporteFactura.html", "w")
            rf.write("<html><head><title>Reporte de Facturas</title></head>")
            rf.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Facturas "Supertienda LA COBANERITA"</h2>')
            rf.write('<h3 style="margin-left:60px">Total Facturas:</h3>')
            rf.write(f'<p style="margin-left:80px">{len(lstFactura)} facturas emitidas en la tienda.</p>')
            rf.write('<p style="text-align:center">__________________________________________________________________________________________</p>')
            rf.write('<h3 style="margin-left:60px">Listado total de facturas:</h3>')
            if lstFactura:
                for facturas in lstFactura:
                    rf.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;><tbody>')
                    rf.write(f'<tr><th>Supertienda "LA COBANERITA"</th></tr>')
                    rf.write(f'<tr><th>Supertienda "LA COBANERITA"</th></tr>')
                    rf.write(f'<tr><td><strong>Factura no.</strong> {facturas.getCodFac()}</td></tr>')
                    rf.write(f'<tr><td><strong>Cliente:</strong> {facturas.getNitClien()}- {facturas.getNomClien()}</td></tr>')
                    rf.write(f'<tr><th>Lista de compra:</th></tr>')
                    for compras in facturas.getLstCompra():
                        rf.write(f'<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;{compras}</td></tr>')
                    rf.write(f'<tr><td><strong>Total:</strong> Q{facturas.getTotal()}</td></tr>')
                    rf.write(f'<tr><td><strong>Empleado encargado</strong>: {facturas.getCodEmp()}- {facturas.getNomEmp()}, {facturas.getTipEmp()}</td></tr>')
                    rf.write(f'<tr><td><strong>En caja no.:</strong> {facturas.getNoCaja()}</td></tr>')
                    rf.write('</tbody></table><br>')
            else:
                rf.write('<p style="text-align:center">Aún no existen facturas registradas...</p>')
            rf.write('</body></html>')
        except EOFError:
            print("[ERROR]-No ha sido posible cargar el archivo.")
        finally:
            rf.close()
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()

    #---REPORTE DE FACTURAS POR CLIENTE---
    def reporteFacturaCliente(self):
        global lstFactura
        os.system("cls")
        #---Importar datos de facturas a la lista.---
        archivoFactura = open("factura.pkl", "ab+")
        archivoFactura.seek(0)
        try:
            lstFactura = pickle.load(archivoFactura)
            print(f"[INFO]-Se cargaron {len(lstFactura)} facturas.")
        except EOFError:
            print("[ADVERTENCIA]-No existen facturas registadas.")
        finally:
            archivoFactura.close()
        
        global lstCliente
        #---Importar datos de empleados a la lista.---
        archivoCliente = open("cliente.pkl", "ab+")
        archivoCliente.seek(0)
        try:
            lstCliente = pickle.load(archivoCliente)
            print(f"[INFO]-Se cargaron {len(lstCliente)} clientes.")
        except EOFError:
            print("[ADVERTENCIA]-No existen clientes registados.")
        finally:
            archivoCliente.close()
        repClien = False

        while True:
            try:
                nitClien = int(input("\nIngrese el NIT del cliente: "))
            except ValueError:
                print("[ADVERTENCIA]-El NIT debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break
        for facturas in lstFactura:
            if facturas.getNitClien() == nitClien:
                repClien = True

        if repClien == True:
            try:
                print("\n[INFO]-Reporte HTML actualizado.")
                rf = open("reporteFacturaCliente.html", "w")
                rf.write("<html><head><title>Reporte de Facturas</title></head>")
                rf.write('<body style="background-color:#E5E4E2"><h2 style="text-align:center;margin-top:20px;">Reporte de Facturas "Supertienda LA COBANERITA"</h2>')
                rf.write('<h3 style="margin-left:60px">Total Facturas:</h3>')
                rf.write(f'<p style="margin-left:80px">{len(lstFactura)} facturas emitidas en la tienda.</p>')
                rf.write('<p style="text-align:center">__________________________________________________________________________________________</p>')
                rf.write('<h3 style="margin-left:60px">Listado total de facturas:</h3>')
                if lstFactura:
                    for facturas in lstFactura:
                        if facturas.getNitClien() == nitClien:
                            rf.write('<table style="border:2px solid black;margin-left:auto;margin-right:auto;padding:2px;border-spacing:20px;background-color:#FFFFFF;><tbody>')
                            rf.write(f'<tr><th>Supertienda "LA COBANERITA"</th></tr>')
                            rf.write(f'<tr><th>Supertienda "LA COBANERITA"</th></tr>')
                            rf.write(f'<tr><td><strong>Factura no.</strong> {facturas.getCodFac()}</td></tr>')
                            rf.write(f'<tr><td><strong>Cliente:</strong> {facturas.getNitClien()}- {facturas.getNomClien()}</td></tr>')
                            rf.write(f'<tr><th>Lista de compra:</th></tr>')
                            for compras in facturas.getLstCompra():
                                rf.write(f'<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;{compras}</td></tr>')
                            rf.write(f'<tr><td><strong>Total:</strong> Q{facturas.getTotal()}</td></tr>')
                            rf.write(f'<tr><td><strong>Empleado encargado</strong>: {facturas.getCodEmp()}- {facturas.getNomEmp()}, {facturas.getTipEmp()}</td></tr>')
                            rf.write(f'<tr><td><strong>En caja no.:</strong> {facturas.getNoCaja()}</td></tr>')
                            rf.write('</tbody></table><br>')
                else:
                    rf.write('<p style="text-align:center">Aún no existen facturas registradas...</p>')
                rf.write('</body></html>')
            except EOFError:
                print("[ERROR]-No ha sido posible cargar el archivo.")
            finally:
                rf.close()
        else:
            print("\nEl cliente no ha sido registrado o aún no cuenta con facturas emitidas.")
        print("\nPresione 'ENTER' para regresar...")
        msvcrt.getch()