import datetime
import abc
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
# Resolvendo a Atividade de CLASSES ABSTRATAS

# 1. Torne a classe Conta abstrata
class Conta(abc.ABC):


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

        return self.__saldo
    
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
    

    #Este metodo faz parte da resolução do exercicio de Herança e Polimorfismo.


 
    """ 
        1. Adicione na classe Conta um novo método chamado atualiza()* que atualiza a conta de acordo
        com a taxa percentual:

    """  
    # 1 Tornar o método atualizar() abstrato
    @abc.abstractmethod 
    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa



    def __str__(self):
        return f'Nome: {self.__titular}'


"""
    Crie a classe ContaCorrente no arquivo conta.py e faça com que ela seja subclasse (filha) da
    classe Conta
"""

class ContaCorrente(Conta):

    def __init__(self, numero, Cliente, saldo=0):
        super().__init__(numero, Cliente, saldo)

    # Reescreva o método atualiza() na classe ContaCorrente , 
    # a ContaCorrente deve atualizar-se com o dobro da taxa
    def atualiza(self, taxa):
        return super().atualiza(taxa * 2)

    """
    Na classe ContaCorrente , reescreva o método deposita() para descontar a taxa bancária de
    dez centavos:
    """
    def deposita_valor(self, num, valor):
        return super().deposita_valor(num, valor - 0.10)
"""
Crie a classe ContaPoupanca no arquivo conta.py e faça com que ela seja subclasse (filha) da
classe Conta :
"""
class ContaPoupanca(Conta):

    def __init__(self, numero, Cliente, saldo=0):
        super().__init__(numero, Cliente, saldo)
    

    def atualiza(self, taxa):
        return super().atualiza(taxa * 3)


# 5. Crie uma classe chamada ContaInvestimento :
class ContaInvestimento(Conta):
    
    def __init__(self, numero, Cliente, saldo=0):
        super().__init__(numero, Cliente, saldo)
    """
    7. Não conseguimos instanciar uma ContaInvestimento que herda Conta sem implementar o
    método abstrato atualiza() . Vamos criar uma implementação dentro da classe
    ContaInvestimento : 
    """

    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa * 3





if __name__ == '__main__':

    """
    3. Tente instância uma Conta :
    Ao tentar instanciar uma conta , o programa retorna um erro:
    conta = Conta(456,'Vinicus',1500)
    TypeError: Can't instantiate abstract class Conta with abstract method atualiza()
    Que eu não posso instanciar uma class que contem um metodo abstrato nesse caso o atualiza
    conta = Conta(456,'Vinicus',1500)
    """

    """
    4. Instancie uma ContaCorrente e uma ContaPoupanca e teste o código chamando o método
    atualiza() . 
    """
    contaCorr = ContaCorrente(789,'maria',4000)
    contaPoup = ContaPoupanca(345,'Marlon',3000)

    #6. Instancie uma ContaInvestimeto :
    contInv =ContaInvestimento(790,'Vinicius',3000)




    contaCorr.atualiza(0.03)
    contaPoup.atualiza(0.06)

    print(contaCorr.saldo)
    print(contaPoup.saldo)

    #8. Agora teste instanciando uma ContaInvestimento e chame o método atualiza() :
    contInv.deposita_valor(789,1000)
    contInv.atualiza(0.01)
    print(f'Saldo da conta de investimento {contInv.saldo}')