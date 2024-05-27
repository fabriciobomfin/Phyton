import os
os.system("cls || clear")

# Criando uma constante para a quantidade de notas
QUANTIDADE_NOTAS = 3

# Criando uma lista para armazenar as notas
notas = []

# Recebendo as notas do usuário
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

# Calculando a média das notas
media = sum(notas) / QUANTIDADE_NOTAS

# Exibindo as notas para o usuário
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota {i + 1}: {notas[i]}")

# Exibindo as notas usando um loop ForEach
for nota in notas:
    print(f"Nota: {nota}")

# Exibindo a média das notas
print(f"Média das notas: {media:.2f}")
