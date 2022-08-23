## classes é uma estrutura que abstrai um conjunto de objetos com caracteristicas

## um objeto é uma instancia de uma classe 
    ## ocupa memória
    ## seus metodos ocupam CPU

print('Estudando POO em python')

class Conta:

    def __init__(self,titular, numero, saldo): # é chamado quando a classe é instanciada(chamada)
       ## atributos da classe conta
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
    def sacar(self):
        print(f'Saldo em conta: {self.saldo}')
        sald = int(input('Informe o valor a ser sacado:'))
        if sald < self.saldo:
            novoSaldo = self.saldo -  sald
            print(f'valor em conta: {self.saldo}')
            print(f'Voce saco : {sald}')
            print('valor sacado com sucesso!!')
            self.saldo = novoSaldo
        if sald > self.saldo:
            print('Impossivel sacar, valor maior que o da sua conta!!')
    def depositar(self):
        deposito = int(input('informe o valor a ser depositado: '))
        acrescimo = self.saldo + deposito

        self.saldo += acrescimo
        print(f'Voce depositou {deposito}')
    
    def ConsultaSaldo(self):
        print(f'Titular: {self.titular}')
        print(f'Numero da Conta: {self.numero}')
        print(f'Saldo em conta: {self.saldo}')
    
    def Transfere(self,destino):
        trasfere = int(input('Informe o valor a ser transferido: '))
        retirou = self.sacar(trasfere)
        if retirou == False :
            return False
        else:
            destino.depositar(trasfere)
            return True

t= 'vinicius'
n = '1234'
s = 0
c1 = Conta(t, n, s)

#c1.sacar()
c1.depositar()

j = 'Angela'
x = 0
k = '4566'
c2  = Conta(j, k, x)
c1.Transfere(c2)

c2.ConsultaSaldo()
c1.ConsultaSaldo()
