class Cliente:
    
    def __init__(self, nome, sobre_nome, cpf):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.cpf = cpf
    
    # metodo que retorna uma string de cliente
    def __str__(self):
        return f'\n\tNome: {self.nome}\n\tSobre Nome:{self.sobre_nome}\n\tCPF: {self.cpf}'

class Conta:

    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
    
    def listaConta(self):
        print(f'\nNumero: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}\n')
    
    def sacar_valor(self,num, valor):
        if valor < self.saldo and num == self.numero:
            self.saldo -= valor
            return True
        else:
            print('Impossivel sacar o valor')
            return False
    
    def deposita_valor(self,num, valor):
        if num == self.numero:
            self.saldo += valor
        

    def transfere(self, destino, valor):
            self.sacar_valor(valor)
            destino.saldo += valor
            

    def __str__(self):
        return f'Nome: {self.titular}'