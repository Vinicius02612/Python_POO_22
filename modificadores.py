class Conta:

    def __init__ (self,numero, titular, saldo = 0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def listaSaldo(self):
        print(f'Nº {self.__numero} \n Titular {self.__titular} \n Saldo: {self.__saldo}')
    @property
    def saldo(self):
        return self.__saldo

c1 = Conta(789, 'Vinicius', 500.00)

c1.saldo