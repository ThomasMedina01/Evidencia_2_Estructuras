import time
from os import system,name

class Validacion:
    
    @staticmethod
    def limpiar_pantalla():
        if name == "nt":
            system("cls")
        else:
            system("clear")
    
    @staticmethod
    def entero (numero):
        try:
            numero = int(numero)
            if numero in range(1,4):
                return numero
            else:
                print(f"ATENCIÓN: Debe ingresar un número entero (1, 2 o 3).")
                return False
        except:
            print(f"ATENCIÓN: Debe ingresar un número entero (1, 2 o 3).")
            return False
        
    @staticmethod
    def cantidad(numero):
        try:
            numero = int(numero)
            return numero
        except:
            print(f"ATENCIÓN: Debe ingresar un número entero.")
            return False
        
    @staticmethod
    def precio(numero):
        try:
            numero = float(numero)
            return numero
        except:
            print(f"ATENCIÓN: Debe ingresar un número.")
            return False
        
    @staticmethod
    def bloqueo(segundos): 
        while segundos: 
            mins, secs = divmod(segundos, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Demasiados intentos, penalizacion de: ",timer, end="\r") 
            time.sleep(1) 
            segundos -= 1

        

            
        
        
    
    
