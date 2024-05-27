from Modelos.Menu import Menu_Principal
from Modelos.restaurantes import Restaurante
from Modelos.avaliacao import Avaliacao

def main():
    opcao_escolhida = -1
    while opcao_escolhida != 0:
        Menu_Principal.listar_menu()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if(opcao_escolhida == 1):
                Restaurante.cadastrar_restaurante(Restaurante)
            elif(opcao_escolhida == 2):
                Restaurante.listar_restaurantes(Restaurante)
            elif(opcao_escolhida == 3):
                Restaurante.alternar_estado(Restaurante)
            elif(opcao_escolhida == 4):
                Restaurante.receber_avaliacao(Restaurante)
            else:
                pass
        except:
            pass

if __name__ == '__main__':
    main()