class Cliente:
    def __init__(self,dni,nomyape,fnac,monto):
        self.__dni = dni 
        self.__nomyape = nomyape     
        self.__fnac = fnac
        self.__monto = 0

#Muestra el nombre del cliente
    def verNom(self):
        return self.__nomyape

#Muestra el D.N.I del cliente
    def verDni(self):
        return self.__dni

#Muestra la fecha nacimiento del cliente
    def verFnac(self):
        return self.__fnac

#Modifica el monto del cliente
    def verMonto(self):
        return self.__monto

#Modifica el nombre del cliente
    def modNom(self,otro):
      self.__nomyape = otro

#Modifica el D.N.I del cliente
    def modDni(self,otro):
        self.__dni = otro

#Modifica la fecha nacimiento del cliente
    def modFnac(self,otro):
        self.__fnac = otro

#Modifica el monto del cliente
    def modMonto(self,otro):
        self.__monto += otro