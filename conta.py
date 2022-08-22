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
        self.data = datetime.datetime.today
        self.transacao =  []

    def add_transacao(self, t):
        self.transacao.append(t)
    
    def mostraHistorico(self):
        print(f'data de abertura:{self.data} ')
        print(f'trasação:')
        for i in self.transacao:
            print(f'-, {i}')

class Conta:

    def __init__(self, numero, Cliente, saldo=0):
        self.numero = numero
        self.titular = Cliente
        self.saldo = saldo
        self.historico =  Historico()
        
    
    def listaConta(self):
        print(
            f'\nNumero: {self.numero}\n'
            f'Titular: {self.titular}\n'
            f'Saldo: {self.saldo}\n')
    
    def sacar_valor(self,num, valor):
        if valor < self.saldo and num == self.numero:
            self.saldo -= valor
            self.historico.mostraHistorico()
            self.historico.add_transacao(f'saque de {valor}')
            return True
        else:
            print('Impossivel sacar o valor')
            return False
    
    def deposita_valor(self,num, valor):
        if num == self.numero:
            self.saldo += valor
            self.historico.mostraHistorico()
            self.historico.add_transacao(f'deposito de {valor}')
 
        

    def transfere(self, destino, valor):
            self.sacar_valor(valor)
            destino.saldo += valor
            self.historico.mostraHistorico()
            self.historico.add_transacao(f'transferencia de {valor}')
            

    def __str__(self):
        return f'Nome: {self.titular}'