from cadastro import cadastrarComponente

estoque = []

while(True):
    op = 0
    opMenu = int(input('\nMenu de opções\n1- Cadastrar componente\n2- Consultar componentes\n0- Sair\n\n'))
    match opMenu:
        case 1:
            opComp = None
            while(True):
                opComp = int(input('\n1- Processador\n2- RAM\n3- Armazenamento\n4- Placa-mãe\n5- Placa de vídeo\n6- Fonte\n7- Gabinete\n\n'))
                cadastrarComponente(opComp, estoque)
                if opComp < 1 or opComp > 7:
                    print('Opção inválida')
                else:
                    break
        case 2:
            for comp in estoque:
                print('====================')
                print(comp.consultarDados())
            print('====================')
        case 0:
            print('Encerrando')
            break
        case _:
            print('Opção inválida')

