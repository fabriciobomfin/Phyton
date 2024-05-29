import os
os.system("cls || clear")

#constante
DUAS_NOTAS = 2

#lista
notas = []

#recebendo as notas
for i in range(DUAS_NOTAS):
    nota = float(input("Digite uma nota: \n"))
    notas.append(nota)

#media
media = sum(notas) / DUAS_NOTAS