#crie um programa que leia 6 números,armazenamento em um vetor e informe quantos são pares e quantos são ímpares.
import os

os.system("cls || clear")

# Criando uma constante.
QUANTIDADES_NUMEROS = 6

# Criando uma lista/vetor.
numeros = []

# Solicitando 6 números para o usuário.
for i in range(QUANTIDADES_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

os.system("cls || clear") # Limpar a tela novamente.

# Exibindo os números para o usuário usando um loop (for).
print("Números digitados:")
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

# Determinando a quantidade de números pares e ímpares.
pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo o total de números pares e ímpares.
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
