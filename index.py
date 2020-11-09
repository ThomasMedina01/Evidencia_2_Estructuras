# Programación del menu de la bisutería.

from Ventas import *
from validaciones import *
import datetime
import sys

separador = ("♦" * 75 + "\n")
try:
    while True:
        print("Registro del detalle de ventas de la bisutería.")
        print(separador)

        menu = ["1.- Registrar una venta.", "2.- Consultar las ventas de un día especifico.", "3.- Salir."]
        for i in menu:
            print(i)
            
        intentos = 4
        opcion = input("Elige la opción deseada: ")
        Validacion.limpiar_pantalla()
        while Validacion.entero(opcion) == False:
            intentos -= 1
            opcion = input(f"Intentalo nuevamente, tienes {intentos} intentos mas: ")
            print(separador)
            if intentos == 1:
                intentos += 3
                Validacion.bloqueo(10)
                print(separador)
                
        if Validacion.entero(opcion) == 1:
            Validacion.limpiar_pantalla()
            print(separador)
            print("Registro de ventas.")
            print(separador)
        
            intentos = 4
            numero_ventas = input("¿Cuantas ventas desea registrar? ")
            print(separador)
            while Validacion.cantidad(numero_ventas) == False:
                intentos -= 1
                numero_ventas = input(f"Intentalo nuevamente, ingresa un número entero, tienes {intentos} intentos mas: ")
                print(separador)
                if intentos == 1:
                    Validacion.bloqueo(10)
                    print(separador)
                    intentos += 3                
                
            
            for x in range(Validacion.cantidad(numero_ventas)):
                descripcion = input("Descripción del articulo: ")
                print(separador)
                intentos = 4
                unidades = input(f"Cantidad de unidades de {descripcion}: ")
                print(separador)
                while Validacion.cantidad(unidades) == False:
                    intentos -= 1
                    unidades = input(f"Intentalo nuevamente, ingresa un número entero, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3

                intentos = 4
                precio = input(f"Precio unitario de {descripcion}: ")
                print(separador)
                while Validacion.precio(precio) == False:
                    intentos -= 1
                    precio = input(f"Intentalo nuevamente, ingresa un valor númerico, tienes {intentos} intentos mas: ")
                    print(separador)
                    if intentos == 1:
                        Validacion.bloqueo(10)
                        print(separador)
                        intentos += 3
                total = Validacion.precio(precio) * Validacion.cantidad(unidades)
                fecha = datetime.date.today()
                venta = Ventas(descripcion, Validacion.cantidad(unidades), Validacion.precio(precio), total, fecha)
                venta.almacen_volatil()
                print(separador)
                print("Venta registrada con exito.")
                print(separador)
                venta.ver_venta()
                print(separador)
                venta.guardar_venta()

        if Validacion.entero(opcion) == 2:
            Validacion.limpiar_pantalla()
            fecha = input("Escriba una fecha(dia/mes/año): ")
            Ventas.consulta(fecha)

        if Validacion.entero(opcion) == 3:
            break
except:
    print(f"Ha ocurrido el siguiente error: {sys.exc_info()[0]}")
  