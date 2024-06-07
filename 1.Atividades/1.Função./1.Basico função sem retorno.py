import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear") #apagar terminal
    print('=' * 30)
    print("---------- SENAI -------------")
    print('=' * 30)

#Solicitando dados para o úsuario.
logoSenai()
nome = input("Digite seu nome: ")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

#Exibindo dados para o usuário
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")