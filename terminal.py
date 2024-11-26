from processador import Processador
from ram import Ram
from armazenamento import Armazenamento
from placaMae import PlacaMae
from placaDeVideo import PlacaDeVideo 
from fonte import Fonte
from gabinete import Gabinete
from cadastro import cadastrarProcessador, cadastrarRam, cadastrarArmazenamento, cadastrarPlacaMae, cadastrarPlacaDeVideo, cadastrarFonte, cadastrarGabinete

estoque = []

def cadastrarComponente(op):
    match op:
        case 1:
            estoque.append(cadastrarProcessador())
        case 2:
            estoque.append(cadastrarRam())
        case 3:
            estoque.append(cadastrarArmazenamento())
        case 4:
            estoque.append(cadastrarPlacaMae())
        case 5:
            estoque.append(cadastrarPlacaDeVideo())
        case 6:
            estoque.append(cadastrarFonte())
        case 7:
            estoque.append(cadastrarGabinete())

while(True):
    op = 0
    opMenu = int(input('\nMenu de opções\n1- Cadastrar componente\n2- Consultar componentes\n0- Sair\n\n'))
    match opMenu:
        case 1:
            opComp = None
            while(True):
                opComp = int(input('\n1- Processador\n2- RAM\n3- Armazenamento\n4- Placa-mãe\n5- Placa de vídeo\n6- Fonte\n7- Gabinete\n\n'))
                cadastrarComponente(opComp)
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

