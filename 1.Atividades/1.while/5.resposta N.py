import os 

os.system('cls || clear')

contadorNotas = 0
soma = 0


while True:
     nota = float(input(f"Digite uma nota : "))
     resposta = input(f"Deseja inserir mais notas ?")
     
     resposta = resposta.upper() #upper converte o texto digitado em  maiúsculo

     if resposta != "n":
        soma += nota
        contadorNotas += 1
     else:
         break

media = soma / contadorNotas
    
print(f"Média: {media}")

