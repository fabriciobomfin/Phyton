
import os

os.system("cls || clear")

#criando uma constante.
QUANTIDADES_NOTAS = 5

# criando uma lista /vetor.
numeros = []

# Solicitando 5 números para o usuário.
for i in range(QUANTIDADES_NOTAS):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
   
# Encontrando o maior e o menor número na lista
maiorNumero = max(numeros)    
menorNumero = min(numeros) 

os.system("cls || clear") #limpar a tela novamente


#  Exibindo os números para o usuário usando (ForEach)
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")


#Exibindo o maior e  menor número.
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")