#crie um pograma que leia 5 números, armazenando em um vetor e informe qual é o menor número e o maior 
#mostre os números informados pelo usuário.


import os
os.system("cls || clear")


# Criando uma constante
QUANTIDADES_NOTAS = 5

# Criando uma lista / vetor.
notas = []

# Solicitando informações do usuário e atribuindo à variável.
for i in range(QUANTIDADES_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

 # Apagar o terminal.

# Encontrar o menor e o maior número
menor = min(notas)
maior = max(notas)

# Exibir as notas para o usuário
print("Notas informadas:")
for nota in notas:
    print(f"Nota: {nota}")

# Exibir o menor e o maior número
print(f"\nMenor nota: {menor}")
print(f"Maior nota: {maior}")













