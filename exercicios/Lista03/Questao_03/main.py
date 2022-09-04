from Elevador import Elevador

elevador = Elevador(0,0,0,0)
def incializar():
    auxCapacidade = int(input('Informe a capacidade do elevador:'))
    auxTotal = int(input('Informe o total de andares:'))
    elevador.inicializa(auxCapacidade, auxTotal)
    pass   


def entrar():
    elevador.MostraElevador()
    pessoa =  int(input('Informe a quantidade de pessoas: '))
    andar = int(input('Informe o andar em que vc esta: '))
    elevador.Entrar(pessoa,andar)

    pass

def sair():
    elevador.MostraElevador()
    p = int(input('informe a quantas pessoas querem sair: '))
    elevador.Sair(p)
    pass

def subir():
    elevador.MostraElevador()
    andar = int(input('informe o numero andar que voce quer subrir: '))
    elevador.Subir(andar)
    pass

def descer():
    elevador.MostraElevador()
    andar = int(input('Informe o numero do andar que quer descer: '))
    elevador.Descer(andar)
    pass


i = 0
while i >= 0:
    print(
    '\n'
    '1 - Inicializar \n'
    '2 - Entrar \n'
    '3 - Subir \n'
    '4 - Desce \n'
    '5 - Sair'
    )

    opc = int(input('Informe a opcao desejada '))


    if opc == 1: 
        incializar()
    if opc == 2: 
        entrar()
    if opc == 3: 
        subir()
    if opc == 4:
        descer()
    if opc == 5:
        sair()
    if opc == 0:
        print('Saindo...')
        break
    i +=1