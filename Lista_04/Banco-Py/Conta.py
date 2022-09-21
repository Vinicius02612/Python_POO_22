

class Conta():
    _total_contas = 0

    def __init__(self,cpf, numero, Cliente,saldo = 0):
        self._cpf = cpf
        self._numero = numero
        self._titular = Cliente
        self._saldo = saldo
        type(self)._total_contas += 1

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        return self._cpf
       

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
        return self._numero
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    
    def sacar(self, valor):
        if valor > self._saldo:
            return 'Impossivel sacar um valor.'
        elif valor < self._saldo:
            self._saldo -= valor
            return self._saldo


    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

    def transferir(self, destino, valor):
        if valor in self._saldo:
            self.sacar(valor)
            destino._saldo += valor

    def imprime(self):
        print(f'Numero : {self._numero}\n'
            f'Titular: {self._titular}\n'
            f'Saldo: {self._saldo}\n')

class ContaCorrente(Conta):
    
    def __init__(self,cpf, numero, Cliente,tipo, saldo=0):
        super().__init__(cpf,numero, Cliente, saldo)
        self._tipo = tipo

    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tp):
        self._tipo = tp
        return self._tipo
    

    def imprime(self):
        print(f'\t\nNumero : {self._numero}\n'
            f'\t\nTitular: {self._titular}\n'
            f'\t\nSaldo: {self._saldo}\n'
            f'\t\nTipo: {self._tipo}\n')

    def __repr__(self):
        return f'\t\nNumero:{self._numero} \t\nTitular: {self._titular} \t\nSaldo: {self._saldo} \t\nTipo: {self._tipo}\n'


"""    def tributacao(self):
        return self._saldo  - 0.10
"""

class ContaPoupanca(Conta):
    def __init__(self,cpf, numero, Cliente,tipo, saldo=0):
        super().__init__(cpf,numero, Cliente, saldo)
        self._tipo = tipo
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tp):
        self._tipo = tp
        return self._tipo

    def imprime(self):
        print(f'\nNumero : {self._numero}\n'
            f'\nTitular: {self._titular}\n'
            f'\nSaldo: {self._saldo}\n'
            f'\nTipo: {self._tipo}')

                
    def __repr__(self):
        return f' \nNumero: {self._numero} \nTitular: {self._titular} \nSaldo: {self._saldo} \nTipo: {self._tipo}\n'
