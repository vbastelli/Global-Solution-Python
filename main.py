from textos import texto_drone, texto_sobrenos, produtos_e_servicos
import textos
from dados import mostrar_dados
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def menu():
    print("1. Informações sobre nosso drone. ")
    print("2. Sobre nós.")
    print("3. Serviços e produtos. ")
    print("4. Contato")
    print("5. Dados sobre o oceano")
    escolha = input("Escolha uma das opções. ")
    return escolha


def servicos():
    print("1. Sensores Marinhos Avançados")
    print("2. Drones Aquáticos e Aéreos")
    print("3. Plataforma de Visualização de Dados")
    print("4. Engajamento e Educação")
    opcao = int(input("Escolha uma opção: "))

    while not (opcao >= 1 and opcao <= len(produtos_e_servicos)):
        print("Opção inválida.")
        opcao = int(input("Escolha uma opção: "))

    titulo, texto = produtos_e_servicos[opcao - 1]
    print(" ")
    print(titulo)
    print(texto)
    print(" ")
    return input("Para ver mais serviços pressione '1', para reiniciar pressione '2'. ")


def reiniciar():
    print(" ")
    input("Aperte enter para reiniciar o programa. ")
    clear()
    programa()


def programa():
    clear()
    print("Seja bem vindo a AquaDrone Innovations!")

    escolha = menu()

    if escolha == "1":
        print(texto_drone)
        reiniciar()

    elif escolha == "2":
        print(texto_sobrenos)
        reiniciar()

    elif escolha == "3":
        opcao2 = servicos()
        while opcao2 == '1':
            opcao2 = servicos()
        programa()

    elif escolha == "4":
        print("Nos contate em nosso email: aquadrone@innovations.com")
        reiniciar()

    elif escolha == "5":
        mostrar_dados()
    reiniciar()


programa()


