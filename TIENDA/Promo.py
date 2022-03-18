class Promo:
    def __init__(self,cant_desc,cod_prod):
       self.__cant_desc = cant_desc
       self.__cod_prod = cod_prod

#Muestra el codigo del producto     
    def VerCod_prod(self):
            return self.__cod_prod

#Muestra el porcentaje de descueto
    def VerCantDesc(self):
            return self.__cant_desc

#Modifica el codigo del producto
    def ModCodp(self,otro):
        self.__cod_prod = otro

#Modifica el porcentaje de descueto
    def ModCantDesc(self,otro):
            self.__cant_desc = otro



