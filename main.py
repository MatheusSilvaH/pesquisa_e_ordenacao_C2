from random import *
from time import time
import sys
from steps import cem_elementos, mil_elementos, dez_mil_elementos, cem_mil_elementos, um_milhao_elementos


def main():
    opcao = "1"
    while opcao != "0":
        print('''
        Escolha uma opcao de vetor:
        
        1- Cem Elementos
        2- Mil Elementos
        3- Dez Mil Elementos
        4- Cem Mil Elementos
        5- Um Milhao Elementos
        0- Sair
        ''')
        opcao = input()
        if opcao == "1":
            cem_elementos()
        elif opcao == "2":
            mil_elementos()
        elif opcao == "3":
            dez_mil_elementos()
        elif opcao == "4":
            cem_mil_elementos()
        elif opcao == "5":
            um_milhao_elementos()
        elif opcao == "0":
            print("Cabo")
        else:
            print("Errou feio, errou rude, digita o numero certo")


if __name__ == "__main__":
    main()
