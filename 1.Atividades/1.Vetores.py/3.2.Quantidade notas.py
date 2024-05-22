
import os
os.system("cls || clear")

#criando uma constante
QUANTIDADES_NOTAS = 3

# criando uma lista /vetor.

notas = []
#soma = 0
# criando uma lista / vetor.
for i in range(QUANTIDADES_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
  
media = sum(notas) / QUANTIDADES_NOTAS

# exibindo as notas para o úsuario
for i in range(QUANTIDADES_NOTAS):
    print(f"Nota: {notas[i]}")

# ForEach
for nota in notas:
    print(f"Notas: {nota}")

    






