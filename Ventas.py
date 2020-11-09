import pandas as pd
import os
import sys

articulos = list()
unidades = list()
precios = list()
montos = list()
fechas = list()

class Ventas:
    
    def __init__ (self, descripcion, cantidad, precio_unitario, total, fecha):
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__total = total
        self.__fecha = fecha
        
    @property
    def descripcion(self):
        return self.__descripcion
    
    @property
    def cantidad(self):
        try:
            self.__cantidad == int(self.__cantidad)
            return self.__cantidad
        except ValueError:
            return False
    
    @property
    def precio_unitario(self):
        try:
            self.__precio_unitario == float(self.__precio_unitario)
            return self.__precio_unitario
        except ValueError:
            return False
        
    
    @property
    def total (self):
        return self.__total
    
    @property
    def fecha (self):
        return self.__fecha
#-------------------------------------------------------------------------------------------------------------------

    @cantidad.setter
    def cantidad(self, valor):
        cantidad = valor
            
    @precio_unitario.setter
    def precio_unitario(self, valor):
        self.__precio_unitario= valor
            
    @total.setter
    def total(self,valor):
        total = valor
        
        
    @fecha.setter
    def fecha(self,valor):
        self.__fecha = valor
        
    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor
      
    @staticmethod
    def comprobacion_precio (instancia):
        if instancia != False:
            return instancia
        while instancia == False:
            nuevo = input("Hubo un error, intentalo nuevamente: ")
            try:
                nuevo = float(nuevo)
                instancia = nuevo
                return instancia
            except:
                print(f"ATENCIÓN: Debe ingresar un número.")
                
    @staticmethod
    def comprobacion_cantidad(instancia):
        if instancia != False:
            return instancia
        while instancia == False:
            nuevo = input("Hubo un error, intentalo nuevamente: ")
            try:
                nuevo = int(nuevo)
                instancia = nuevo
                return instancia
            except:
                print(f"ATENCIÓN: Debe ingresar un número.")

    @staticmethod
    def consulta(a):
        try:
            df = pd.read_csv('Ventas.csv')
            dfl = pd.DataFrame(df)
            print(dfl[dfl.Fecha == a])
        except:
            print(f"Ha ocurrido un error: {sys.exc_info()[0]}")

    def almacen_volatil (self):
        articulos.append(self.__descripcion)
        unidades.append(self.__cantidad)
        precios.append(self.__precio_unitario)
        montos.append(self.__total)
        fechas.append(self.__fecha)
    
    def ver_venta (self):
        print(f"Articulo: {self.__descripcion}")
        print(f"Número de unidades: {self.__cantidad}")
        print(f"Precio unitario: {self.__precio_unitario}")
        print(f"Monto total: {self.__total}")
        print(f"Fecha de registro: {self.__fecha}")
        
    def guardar_venta(self):
        zipper = list(zip(articulos, unidades, precios, montos, fechas))
        df_zipper = pd.DataFrame(zipper)
        df_zipper.rename(columns={0:"Articulos", 1:"Unidades", 2:"Precio_unitario", 3:"Total", 4:"Fecha"}, inplace=True)
        df_zipper.to_csv("ventas.csv", mode="a", index = None, header=not os.path.isfile("ventas.csv"))
   
        
#-------------------------------------------------------------------------------------------------------------------




            
    

    
    
  