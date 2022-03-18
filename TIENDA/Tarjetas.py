class Tarjetas():
    def __init__(self,nomt,canfpag,recarpag,banc):
        self.__nomt = nomt
        self.__canfpag = canfpag
        self.__recarpag = recarpag
        self.__banc = banc
        self.__monto_total = 0
        
    def __init__(self,nomt,canfpag,recarpag,banc):
        self.__nomt = nomt
        self.__canfpag = canfpag
        self.__recarpag = recarpag
        self.__banc = banc
        self.__monto_total = 0

#Muestra el nombre de la tarjeta        
    def vernomt(self):
            return self.__nomt

#Muestra las cantidad de formas de pago de la tarjeta( las Cuotas)
    def vercanfpag(self):
            return self.__canfpag

#Mestra el costo del finaciamiento de las cuotas(interes)
    def verrecarpag(self):
            return self.__recarpag

#Mustra el nombre del banco 
    def verbanc(self):
        return self.__banc
#Mustrar monto total
    def vermonto_total(self):
        return self.__monto_total

#Modifica el nombre de la tarjeta
    def modnomt(self,otro):
        self.__nomt = otro

#Modifica la cantidad de formas de pago de la tarjeta( las Cuotas)
    def modcanfpag(self,otro):
        self.__canfpag = otro

#Modifica el costo del finaciamiento de las cuotas
    def modrecarpag(self,otro):
        self.__recarpag = otro

#Modifica el nombre del banco
    def modbanc(self,otro):
        self.__banc = otro

#Modificar monto total
    def modmonto_total(self,otro):
        self.__monto_total += otro

