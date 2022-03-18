class Producto:
    def __init__(self,nom,cod,pre,cant,desc,porcen_descu):
        self.__nom = nom
        self.__cod = cod
        self.__pre = pre
        self.__cant = cant
        self.__desc = desc
        self.__porcen_descu = 0
        
    def __init__(self,nom,cod,pre,cant,desc):
        self.__nom = nom
        self.__cod = cod
        self.__pre = pre
        self.__cant = cant
        self.__desc = desc
        self.__porcen_descu = 0  

#Muestra el nombre del producto
    def verNom(self):
            return self.__nom

#Muestra el codigo del producto
    def verCodP(self):
            return self.__cod

#Muestra el precio del producto
    def verPre(self):
            return self.__pre

#Muestra la cantidad de unidades del producto
    def verCant(self):
            return self.__cant

#Muestra una descripcion del producto
    def verDesc(self):
            return self.__desc

#Ver % de descuent
    def verporcen_descu(self):
        return self.__porcen_descu

#Modifica el nombre del producto
    def modNom(self,otro):
        self.__nom = otro

#Modifica el codigo del producto
    def modCod(self,otro):
            self.__cod = otro

#Modifica el precio del producto
    def modPre(self,otro):
            self.__pre = otro

#Modifica la cantidad de unidades del producto
    def modCant(self,otro):
            self.__cant = otro

#Modifica la descripcion del producto
    def modDesc(self,otro):
            self.__desc = otro
        
 #Modificar % de descuento
 
    def modporcen_descu(self,otro):
        self.__porcen_descu = otro

      
