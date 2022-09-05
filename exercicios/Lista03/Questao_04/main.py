from Controle import ControleRemoto


ctrl = ControleRemoto()


i = 0
while i >= 0:
    print(
    '\n'
    '1 - Mudar canal \n'
    '2 - Diminuir canal \n'
    '3 - Aumenta Volume \n'
    '4 - Diminuir Volume \n'
    '5 - Procurar Canal \n'
    '6 - Sair \n'
    )
    opc = int(input('Informe a opcao desejada '))
    if opc == 1: 
       ctrl.AumentaCanal()
    if opc == 2: 
        ctrl.DiminuiCanal()
    if opc == 3: 
        ctrl.AumentarVolume()
    if opc == 4:
        ctrl.ReduzirVolume()
    if opc == 5:
        ctrl.ProcuraCanal()
    if opc == 0:
        print('Saindo...')
        break
    i +=1