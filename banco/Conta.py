import datetime

class Historico:

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacao = []

    def imprime(self):
        print(f'Data de transacão {self.data_abertura}')
        print('Transação => ')
        for i in self.transacao:
            print('==',i)

    
    def __str__(self) -> str:
        return  f'{self.transacao}'



class Conta:
    _total_contas = 0

    __slot__ = ['_numero', '_cliente', '_saldo', '_limite']
    
    def __init__(self,numero,cliente, saldo, limite = 1000):
        self._numero = numero
        self._titular = cliente
        self._saldo =saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1 
    
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
    def titular(self, ttl):
        self._titular = ttl
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, sld):
        if self._saldo < 0:
            return 'saldo não pode ser negativo'
        else: 
            self._saldo = sld
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, lmt):
        self._limite = lmt
        return self._limite


    def deposita(self, valor):
        if valor > self._limite:
            return 'Valor acima do limite'
        elif self._saldo < valor:
            self._saldo += valor
            self._historico.transacao.append(f'{datetime.datetime.now()} - Deposito de {valor}  ')
        else:
            return 1
    
    def sacar(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self._historico.transacao.append(f'{datetime.datetime.now()} - Saque de {valor} ')
            return True
    
    def transfere(self, valor, destino):
        retirou = self.sacar(valor)
        if retirou == False:
            return f'Não foi possivel transferir'
        if retirou == True:
            destino.saldo += valor
            self.historico.transacao.append(f'{datetime.datetime.now()}Transferencia de {valor}  ')
            return f'voce transferiru {valor} para {destino}'

    
    
    def extrato(self):
        self._historico.transacao.append(f'Pedido de Extrato em: {datetime.datetime.now()}')
        return f'Numero: {self.numero}\n Titular: {self.titular}\nsaldo: {self.saldo}\nLimite: {self.limite}\n\n\n'

    @staticmethod
    def get_total_contas():
        return Conta._total_contas


    def __str__(self):
        return f'{self._numero}, {self._titular}, {self._saldo}, {self._limite}'
        




