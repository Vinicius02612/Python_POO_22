from Agenda import Agenda


dic_agenda = {}


def ArmazenaPessoa():
    nome = input('informe o seu nome: ')
    idade = int(input('informe sua idade: '))
    altura = float(input('Informe a sua altura: '))

    agenda = Agenda(nome, idade, altura)
    dic_agenda[nome] = agenda

    return dic_agenda

def removePessoa():
    n = input('informe o nome a ser excluido: ')
    if n in dic_agenda:
        del dic_agenda[n]

def buscaPessoa():
    n = input('Informe o nome a pessoa que procura: ')
    if n in dic_agenda:
        print(dic_agenda[n])

def getAgenda():
    for i in dic_agenda.values():
        i.ImprimeAgenda()



## criando o menu
i = 0
while i >= 0:
    print(
    '\n'
    '1 - Armazena Pessoa \n'
    '2 - Remover uma Pessoa \n'
    '3 - Buscar uma Pessoa \n'
    '4 - Imprimir Pessoas \n'
    '0 - Sair'
    )

    opc = int(input('Informe a opcao desejada '))


    if opc == 1: ## criar conta
        ArmazenaPessoa()

    if opc == 2: ## listar contas criadas
        removePessoa()
    if opc == 3: 
        buscaPessoa()
    if opc == 4:
        getAgenda()
    if opc == 0:
        print('Saindo...')
        break
    i +=1