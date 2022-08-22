from conta import Conta,Cliente
import random
dic_contas = {}

def criarConta():
    name = input('Informe seu nome: ')
    surName = input('Seu sobre nome: ')
    cpf = input('Informe seu cpf: ')

    cliente = Cliente(name, surName,cpf)
    numero = random.randint(100,999)

    c = Conta(numero, cliente)
    dic_contas[numero] = c

def listarConta():
    for y in dic_contas.values():
        y.listaConta()

    
def sacarValor():
    valor = float(input('informe o valo a ser sacado:'))
    num = int(input('informe o numero da conta: '))

    for  y in dic_contas.values():
        y.sacar_valor(num, valor)
    
def depositarvalor():
    valor = float(input('informe o valor a ser depositado: '))
    num = int(input('Informe o numero da conta: '))
    for j in dic_contas.values():
        j.deposita_valor(num, valor)
    print('Desposito relaziado com sucesso...')

def excluirConta():
    num = int(input('Informe o numero da conta: '))
    if num in dic_contas:
        del dic_contas[num]
        print('Conta excluida com sucesso...')

def trasnferirValor():
    num = int(input('Informe o numero da conta de origem: '))
    num_2 = int(input('Informe o numero da conta de destino'))
    valor = float(input('Informe o valor: '))
    if num in dic_contas:
        dic_contas[num].transfere(dic_contas[num_2], valor)
            
## criando o menu
i = 0
c = 0
while i >= 0:
    print(
    '\n1 - Criar uma conta \n'
    '2 - Lista Contas \n'
    '3 - Sacar um Valor \n'
    '4 - Depositar um valor \n'
    '5 - Excluir Conta \n'
    '6 - Tranferir um valor\n'
    '0 - Sair'
    )

    opc = int(input('Informe a opcao desejada '))


    if opc == 1: ## criar conta
        criarConta()

    if opc == 2: ## listar contas criadas
        listarConta()
    if opc == 3: ## Sacar valor da conta
        print('Escolha uma conta para sacar um valor \n ')
        listarConta()
        sacarValor()
    if opc == 4: ## Depositar valor da conta
        print('Escolha um conta para depositar um valor \n ')
        listarConta()
        depositarvalor()
    if opc == 5: ## Excluir conta
        print('Escolha um conta para excluir\n ')
        listarConta()
        excluirConta()
    if opc == 6:
        print('Voce escolheu transferir...')
        listarConta()
        trasnferirValor()
    if opc == 0:
        print('Saindo...')
        break
    i +=1