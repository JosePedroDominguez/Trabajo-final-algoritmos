from Cliente import *
from Producto import *
from Promo import *
from Tarjetas import *


class Administracion :
    def __init__(self):
        self.__ListaCliente = []
        self.__ListaPromocion = []
        self.__ListaProducto = []
        self.__ListaTarjeta = []
        self.__carrito = []

      
#Comprobar si existe el producto
    def ExisteProducto(self,cod):
        for x in self.__ListaProducto:
            if x.verCodP() == cod:
                return True
            else:
                return False

#Comprobar si existe el cliente    
    def ExisteCliente(self,dni):
        existe = "no"
        for x in self.__ListaCliente:
            if x.verDni() == dni:
                existe = "si"
        return existe

#Comprobar si existe la tarjeta en el sistema
    def ExisteTarjeta(self,nomt,banc):
            for x in self.__ListaTarjeta:
                if x.vernomt() == nomt and x.verbanc() == banc:
                    return True
                else:
                    return False

#Agregar producto 
    def AgregarProducto(self,producto):
        if isinstance (producto,Producto):
            self.__ListaProducto.append(producto)

#Agregar cliente
    def AgregarCliente(self,cliente):
        self.__ListaCliente.append(cliente)

#Mostrar los productos cargados en el sistema
    def MostrarListaProd(self):
        return self.__ListaProducto

#Mostrar las promociones cargadas en el sistema
    def MostrarListaProm(self):
        return self.__ListaPromocion

#Mostrar los clientes cargados en el sistema
    def MostrarListaCliente(self):
        return self.__ListaCliente

#Mostrar las tarjetas cargadas al sistema
    def verLisTar(self):
            return self.__ListaTarjeta

#Subir una promocion al sistema
    def DarAltaPromo(self,prom):
        if isinstance(prom,Promo):
            self.__ListaPromocion.append(prom)

#Agregar tarjeta
    def AgregarTarjeta(self,tarjetas):
            if isinstance(tarjetas,Tarjetas):
                self.__ListaTarjeta.append(tarjetas)

#Agregar un producto al carro del cliente
    def AgregarAlCarro(self,producto):
        self.__carrito.append(producto)

#Sacar un producto del carro de cliente
    def sacacar(self,producto):
        if (producto,Producto):
            for x in self.__carrito:
                if x.verCodP() == producto.verCodP():
                    self.__carrito.remove(x)

#Muestra el carro del cliente
    def vercar(self):
        return self.__carrito

    def vaciarcarro(self):
        self.__carrito.clear()

#Sacar un producto de la lista de la tienda
    #def baja(self,producto):
        #if (producto,Producto):
            #for x in self.__carrito:
                #if x.verCodP() == producto.verCodP():
                   #self.__ListaProducto.remove(producto)
