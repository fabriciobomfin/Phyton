
import os 

os.system('cls || clear')

QUANTIDADE_NOTAS = 2

soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
     nota = int(input(f"Digite a {i+1}ª nota(entre 0 e 10): \n"))

     if nota < 0 or nota > 10:
        print("Nota inválida. Por favor, tente novamenmte. \n")
     else:
        soma += nota 
        break
    media = soma / QUANTIDADE_NOTAS
    print(f"Média: {media}")