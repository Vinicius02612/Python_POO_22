import abc

class Cliente:

    def __init__(self, nome, sobre_nome, cpf):
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.cpf = cpf
    
    # metodo que retorna uma string de cliente
    def __str__(self):
        return f'\n\tNome: {self.nome}\n\tSobre Nome:{self.sobre_nome}\n\tCPF: {self.cpf}'



#1. Torne a classe Conta abstrata.
class Conta(abc.ABC):
    

    def __init__(self, numero, Cliente, saldo = 0, limite = 250):
        self._numero = numero
        self._titular = Cliente
        self._saldo = saldo
        self._limite = limite

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
      
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
        return self._saldo
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        self._limite = limite
        return self._limite

    def ImprimeConta(self):
        print(f'\nNumero: {self._numero}\n'
            f'\nTitular: {self._titular}\n'
            f'\nSaldo: {self._saldo}\n'
            f'\nLimite de Gasto: {self._limite}\n'
        )
    
    def sacar(self, valor):
        if valor < self._saldo:
            self._saldo -= valor
            return 'Saque realizado com sucesso!'
        elif valor > self._saldo:
            return 'Impossivel realizar o saque, valor acima do esperado'
    
    def deposita(self, valor):
        self._saldo +=  valor
        return 'Deposito realizado com sucesso!'
    
    def transfere(self, destino, valor):
        self.sacar(valor)
        destino._saldo += valor
    
  
    @abc.abstractmethod 
    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa
    

    def __str__(self):
        return f'Nome: {self._titular}'

class ContaCorrente(Conta):
        def __init__(self, numero, Cliente,tipo, saldo=0, limite=250):
            super().__init__(numero, Cliente, saldo, limite)
            self._tipo = tipo

        @property
        def tipo(self):
            return self._tipo
        
        @tipo.setter
        def tipo(self, tipo):
            self._tipo = tipo

        def atualiza(self, taxa):
            self.__saldo += self.__saldo * taxa * 2


class ContaPoupanca(Conta):

    def __init__(self, numero, Cliente,tipo, saldo=0):
        super().__init__(numero, Cliente, saldo, limite=200)
        self._tipo = tipo
    
    @property
    def tipo(self):
            return self._tipo
        
    @tipo.setter
    def tipo(self, tipo):
            self._tipo = tipo

    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa * 2
    

    def __str__(self):
        return f'Tipo: {self._tipo}'



class ContaInvestimento(Conta):
    
    def __init__(self, numero, Cliente,tipo, saldo=0):
        super().__init__(numero, Cliente, saldo,limite=300)
        self._tipo = tipo
    @property
    def tipo(self):
            return self._tipo
        
    @tipo.setter
    def tipo(self, tipo):
            self._tipo = tipo

    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa * 5


    def __str__(self):
        return f'Tipo: {self._tipo}'




if __name__ == '__main__':
#  3. Tente instância uma Conta,O que acontece?
 cliente = Cliente('Vinicius','Nunes','1241515162')
 cliente_2 = Cliente('Flamengo','Mengão','102020034')
# c = Conta('1242-6',cliente,230)

# c.ImprimeConta()
contInvest = ContaInvestimento('1231-5',cliente,'corrente',400)
contInvest.deposita(3000)
contInvest.ImprimeConta()

contInvest_2 = ContaInvestimento('1231-5',cliente_2,'pouança',500)
contInvest_2.deposita(3000)
contInvest_2.ImprimeConta()