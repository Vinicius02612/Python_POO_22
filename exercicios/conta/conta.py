import datetime

class Cliente:

    def __init__(self, nome, sobre_nome, cpf):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.cpf = cpf
    
    # metodo que retorna uma string de cliente
    def __str__(self):
        return f'\n\tNome: {self.nome}\n\tSobre Nome:{self.sobre_nome}\n\tCPF: {self.cpf}'


class Historico:
    def __init__(self):
        self.data = datetime.datetime.today()
        self.transacao =  []

    def add_transacao(self, t):
        self.transacao.append(t)
    
    def mostraHistorico(self):
        print(f'data de abertura:{self.data}')
        print(f'trasação:')
        for i in self.transacao:
            print(f'-, {i}')

class Conta:

    def __init__(self, numero, Cliente, saldo=0):
        self.__numero = numero
        self.__titular = Cliente
        self.__saldo = saldo
        self.historico =  Historico()

    ## getter de saldo
    @property    
    def saldo(self):
        return self.__saldo
     
    ## setter de saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

        return self.__numero
    
    ## getter de numero
    @property
    def numero(self):
        return self.__numero
    
    ## metodo setter do numero
    @numero.setter
    def numero(self,  numero):
       self.__numero = numero
       return self.__numero
    
    ## getter do titular
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
        return self.__titular
    
    def listaConta(self):
        print(
            f'\nNumero: {self.__numero}\n'
            f'Titular: {self.__titular}\n'
            f'Saldo: {self.__saldo}\n')
    
    def sacar_valor(self,num, valor):
        if valor < self.__saldo and num == self.__numero:
            self.__saldo -= valor
 ##          self.__historico.mostraHistorico()
            self.historico.mostraHistorico()
            return True
        else:
            print('Impossivel sacar o valor')
            return False
    
    def deposita_valor(self,num, valor):
        if num == self.__numero:
            self.__saldo += valor
            self.historico.mostraHistorico()
 
    def transfere(self, destino, valor):
            self.sacar_valor(valor)
            destino.__saldo += valor

            self.historico.mostraHistorico()
            
    def __str__(self):
        return f'Nome: {self.__titular}'