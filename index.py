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
  