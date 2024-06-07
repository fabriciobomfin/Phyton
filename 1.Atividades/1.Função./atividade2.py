import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear") # limpar terminal
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def mostrar_tabuada(numero):
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")  #  operação de multiplicação

# Solicitando dados para o usuário.
logoSenai()
numero = int(input("Digite um número: "))  # Convertendo a entrada do usuário para um número inteiro

# Exibindo dados para o usuário
logoSenai()
print("Tabuada:")
mostrar_tabuada(numero)  # Chamar a função corretamente
