
from Conta import Conta
from Cliente import Cliente

cont = Conta('','','','')
class Banco:
    def __init__(self):
        self._clientes = {}
        self._contas = {}
    

    def addCliente(self):

        #criando cliente
        nome = 'Vinicius'
        sobrenome = 'Nunes'
        cpf = '12345'
        usuario = input('usuario:')
        senha = input('12345')
        cli = Cliente(nome, sobrenome,cpf,usuario,senha)
        if cpf in self._clientes.keys():
            return False, 'Cliente ja cadastrado'
        else:
            self._clientes[cpf] = cli
            return True, 'Conta criada com sucesso'

    def addConta(self):
        n = input('informe o cpf do cliente:')
        if n in self._clientes.keys():
            for n in self._clientes.values():
                cliente = n

        numero = input('numero: ')
        saldo = input('saldo: ')
        cont = Conta(numero,cliente, saldo)
        self._contas[numero] = cont
        return cont


    def Depositar(self):
        num = input('Informe o numero da conta: ')
        for num in self._contas.keys():
            if num in self._contas.values():
                    


            
    def BuscarConta(self):
        numero = input('Informe o numero:')
        if numero in self._contas.keys():
            for numero in self._contas.values():
                print(numero)

    def listarContas(self):
        for cont in  self._contas.values():
            print(cont)


    def listarCliente(self):
        for user in self._clientes.values():
            print(user)

    



