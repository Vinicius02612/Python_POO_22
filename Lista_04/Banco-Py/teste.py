""" from Funcionario import Funcionario
from Cliente import Cliente
from Conta import ContaCorrente,ContaPoupanca



dic_funcionario = {} 
dic_cliente = {}
dic_conta_corrente = {}
dic_conta_poupanca = {}

dic_banco = []

def cadastrarFuncionario():
    nome = 'jose'
    cpf = '000.000.000-88'
    data = '23/02/2000'
    salario = 1200.00
    func = Funcionario(nome,cpf,data, salario)
    dic_funcionario[cpf] = func

def cadastrarCliente():
    nome = 'Vinicius'
    cpf = '123'
    data = '23/02/2000'
    profissao = 'dev'
    cliente = Cliente(nome,cpf,data, profissao)
    dic_cliente[cpf] = cliente
    dic_banco.append(dic_cliente)

    opc = int(input('Deseja criar uma conta? 1 - sim 2 - não'))

    if opc == 1:
        while True:
                n =  int(input('Deseja Criar uma conta 1 - Corrente ou 2 - Poupança e  3 - Não '))
                if n == 1:
                    num = 120
                    saldo = 1000
                    tipo = 'Corrente'
                    conta_C = ContaCorrente(cpf, num,cliente,tipo,saldo)
                    num_cpf = input('Informe o seu cpf: ')
                    if num_cpf in dic_conta_corrente.keys():
                        print('Conta Cliente ja existe...')
                        return
                
                    dic_conta_corrente[cpf] = conta_C
                    print('criada com sucesso')
                    dic_banco.append(dic_conta_corrente)
                      
                if n == 2:
                    num = 150
                    saldo = 2000
                    tipo = 'Poupança'
                    conta_P = ContaPoupanca(cpf,num,cliente,tipo,saldo)
                    n = input('Informe o seu cpf:')
                    if n in dic_conta_poupanca.keys():
                        print('Conta Poupança ja existe...')
                        return
                        
                
                    dic_conta_poupanca[num] = conta_P
                    dic_banco.append(dic_conta_poupanca)

               
                if n == 3:
                    break
        
def listarFuncionario():
    for i in dic_funcionario.values():
        i.imprime()

def listaCliente():

    print(f'Dados Bancarios\n {dic_banco} \n')

    for i in dic_cliente.values():
        print(i.imprimeCliente())

 

while True:
    print('1 - Cadastrar Funcionario\n'
        '2 - Cadastrar Cliente \n'
        '3 - Listar Funcionarios\n'
        f'4 - Listar Cliente\n')
    opc = int(input('Informe sua opção: '))
    if opc == 1:
        cadastrarFuncionario()
    if opc == 2:
        cadastrarCliente()
    if opc == 3:
        listarFuncionario()
    if opc == 4:
        listaCliente()




 """