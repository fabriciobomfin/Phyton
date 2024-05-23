#faça um pograma que imprime a tabuada de um número informado pelo usuário de 1 a 10 utilizando uma função para exibir o resultado.
import os


# Função sem retorno.
def logoSenai():
    os.system("cls || clear") #apar terminal
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

#Solicitando dados para o úsuario.
logoSenai()
nome = input("Digite seu nome: ")

logoSenai()
idade = int(input("Digite sua iadade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

#Exibindo dados para o usuário
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")