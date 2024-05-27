import os
os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 3
notas = []

for i in range(QUANTIDADE_DE_NOTAS):
   pergunta = float(input("Digite um número: "))
   notas.append(pergunta)

media = sum(notas) / QUANTIDADE_DE_NOTAS

for i in range(QUANTIDADE_DE_NOTAS):
   print(f"Nota: {notas[i]}")
   print(f"Média: {media}")


