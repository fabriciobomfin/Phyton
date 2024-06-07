import os
os.system("cls || clear")

# criando uma lista /vetor.
notas = []

# criando uma lista / vetor.
for i in range(3):
  nota = float(input("Digite uma nota: "))
  notas.append(nota)

# exibindo as notas para o úsuario
for i in range(3):
    print(f"Nota: {notas[i]}")
