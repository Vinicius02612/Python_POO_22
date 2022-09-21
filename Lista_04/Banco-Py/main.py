
from Funcionario import Funcionario
from Cliente import Cliente,Seguro_de_vida
from Conta import ContaCorrente,ContaPoupanca



dic_funcionario = {} 
dic_cliente = {}
dic_conta_corrente = {}
dic_conta_poupanca = {}
dic_seguros = {}

banco = []

# cadastrando Funcionario
def cadastrarFuncionario():
    nome = 'jose'
    cpf = '000.000.000-88'
    data = '23/02/2000'
    salario = 1200.00
    func = Funcionario(nome,cpf,data, salario)
    dic_funcionario[cpf] = func


# criar conta usando pegando com parametro a opc, o cpf e um objeto Cliente
# o cpf é para usar com chave do dicionário de conta corrente e de conta poupança
# o objeto cliente é para ser passado como parametro para a classe ContaCorrente
def CriarConta(opc,cpf, cliente):
     if opc == 1:
        while True:
                n =  int(input(' Criar uma conta \n(1 - Corrente)\n(2 - Poupança)\n( 3 - Não )\n'))
                if n == 1:
                    num = 160
                    saldo = 1000
                    tipo = 'Corrente'

                    # Aqui eu passo o cpf como paramentro da Class ContaPoupanca para poder verificar se o cliente ja tem uma conta
                    conta_C = ContaCorrente(cpf,num,cliente,tipo,saldo)

                    # verifico se a pessoa ja tem uma conta cadastrada com aquele CPF
                    ver = input('Informe o seu CPF:')
                    if ver in dic_conta_corrente.keys():
                        print('Conta Cliente ja existe...')
                        break
                    else:
                        dic_conta_corrente[cpf] = conta_C
                        print('criada com sucesso!')
                        #Adciono o dicionario de conta corrente dentro da lista de banco
                        banco.append(dic_conta_corrente)
                      
                if n == 2:
                    num = 150
                    saldo = 2000
                    tipo = 'Poupança'

                    # Aqui eu passo o cpf como paramentro da Class ContaPoupanca para poder verificar se o cliente ja tem uma conta
                    conta_P = ContaPoupanca(cpf,num,cliente,tipo,saldo)

                    # verifico se a pessoa ja tem uma conta cadastrada com aquele CPF
                    n = input('informe seu CPF:')
                    if n in dic_conta_poupanca.keys():
                        print('Conta Poupança ja existe...')
                        break
                    else:
                        dic_conta_poupanca[cpf] = conta_P

                        #Adciono o dicionario de conta corrente dentro da lista de banco
                        banco.append(dic_conta_poupanca)
                        print('Conta Criada com sucesso')
                if n == 3:
                    break


def Criar_Seguro_de_Vida(nome, cpf,cliente):
        valorMensal = 130.00
        meses = 12
        valorTotal =valorMensal * meses
        seguro = Seguro_de_vida(nome, cpf, valorMensal, valorTotal)
        cliente.cliente_seguro = seguro
        cliente.cliente_seguro.dados_do_seguro()
    



def cadastrarCliente():
    nome = 'Vinicius'
    cpf = '123'
    data = '23/02/2045'
    profissao = 'dev'
    cliente = Cliente(nome,cpf,data, profissao)
    dic_cliente[cpf] = cliente
    banco.append(dic_cliente)

    opc = int(input('Deseja criar uma conta? 1 - sim 2 - não'))
    if opc == 1:
        CriarConta(opc,cpf,cliente)
    if opc == 2:
        return
    seg =  int(input('Deseja Criar um seguro de vida? 1 - sim e 2 - não'))
    if seg == 1:
        Criar_Seguro_de_Vida(nome, cpf,cliente)
    if seg == 2:
        return



        
def listarFuncionario():
    for i in dic_funcionario.values():
        i.imprime()

def listaCliente():
    for i in dic_cliente.values():
        print(i.imprimeCliente())

    for i in dic_conta_corrente.values():
        print(i.imprime())
    for i in dic_conta_poupanca.values():
        print(i.imprime())

def listarDadosDoBanco():
    print(f'Dados do Banco: {banco}')





while True:
    print(
        '1 - Cadastrar Funcionario\n'
        '2 - Cadastrar Cliente \n'
        '3 - Listar Funcionarios\n'
        '4 - Listar Cliente\n'
        '5 - Listar Dados do Banco\n'
        '6 - sair\n'

    )
    opc = int(input('Informe sua opção: '))
    if opc == 1:
        cadastrarFuncionario()
    if opc == 2:
        cadastrarCliente()
    if opc == 3:
        listarFuncionario()
    if opc == 4:
        listaCliente()
    if opc == 5:
        listarDadosDoBanco()
    if opc == 6:
        break

