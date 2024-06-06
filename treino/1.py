import os
os.system("cls || clear")

#CONSTANTE
DOIS_NUMEROS = 2

#LISTA
notas = []

#pedindo informação
for i in range(DOIS_NUMEROS):
    numero = float(input("Digite um número. \naqui: "))
    os.system("cls || clear")
    notas.append(numero)

    media = sum(notas) / DOIS_NUMEROS

for i in range(DOIS_NUMEROS):
   print(f"Notas inseridas:{notas[i]}")
    