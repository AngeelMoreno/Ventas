import csv
import os

dicVentas = {}
mtzVenta = []
lstVenta_Articulo = []

Id_Venta = 0

while True:
    print("1-   Registrar una venta")
    print("2-   Consultar una venta")
    print("3-   Reporte de ventas por fecha")
    print("4-   Salir")
    Opcion = input("Selecciona una opción: ")
    if Opcion == "4":
        #Backup
        ruta_archivo=os.path.abspath(os.getcwd())
        archivo_respaldo=ruta_archivo+"\\ventas.bak"
        archivo_normal=ruta_archivo+"\\ventas.csv"

        print(archivo_respaldo)
        print(archivo_normal)

        # Si hay archivo de datos.
        if os.path.exists(archivo_normal):
            # verifica si hay respaldo, y lo elimina
            if os.path.exists(archivo_respaldo):
                os.remove(archivo_respaldo)
            # Pasa el archivo normal, para que sea archivo de respaldo
            os.rename(archivo_normal,archivo_respaldo)

        # Genera el archivo CSV.
        f = open(archivo_normal,"w+")
        # Escribir el encabezado.
        f.write("ID | DETALLE_VENTA\n")
        for elemento in dicVentas:
            f.write(f'{elemento}|{dicVentas[elemento]}\n')
        # Cierro el archivo.
        f.close()
        #Salir del programa

        f = open(archivo_respaldo,"w+")
        # Escribo los encabezados de mi CSV
        f.write("ID | DETALLE_VENTA\n")
        # Escribimos en el CSV, a partir de la lista de objetos.
        for elemento in dicVentas:
            f.write(f'{elemento}|{dicVentas[elemento]}\n')
        # Cierro el archivo
        f.close()
        print("SALIENDO...")
        break

    elif Opcion == "1":
        #Registrar una venta
        Id_Venta = Id_Venta + 1
        print("|     Nueva Venta     |")
        mtzVenta.append(input("Ingresa la fecha de la venta (DD/MM/YYYY):"))
        TotalVenta = 0
        Add = "S"
        while Add.upper() == "S":
            lstVenta_Articulo.append(input("Descripcion del articulo: "))
            lstVenta_Articulo.append(int(input("Cantidad de piezas vendidas: ")))
            Precio = float(input("Precio de venta: "))
            lstVenta_Articulo.append(Precio)

            TotalVenta = TotalVenta + Precio
            
            mtzVenta.append(lstVenta_Articulo.copy())
            lstVenta_Articulo.clear()

            Add = input("\n¿Desea agregar otro articulo a la venta?\nS/N: ")
            print()

        dicVentas [Id_Venta] = mtzVenta.copy()
        print(f"MONTO TOTAL A PAGAR DE LA VENTA NO°{Id_Venta}: ${TotalVenta}")
        mtzVenta.clear()
        
    elif Opcion == "2":
        #Consultar una venta
        Id_Venta_Search = int(input("Ingresa el ID de la venta que deseas: "))
        if Id_Venta_Search in dicVentas.keys():
            print("\n",dicVentas[Id_Venta_Search])
        else:
            print("ERROR: El ID ingresado no existe dentro de los registros...")
    
    elif Opcion == "3":
        Fecha_Busqueda = input("Ingresa la fecha de la venta (DD/MM/YYYY): ")
        for venta in range(0,len(dicVentas)):
            if (dicVentas[venta+1][0] == Fecha_Busqueda):
                print(dicVentas[venta+1])
    print()