
import os 

os.system('cls || clear')

# Inicializando as variáveis
soma_pares = 0
quantidade_pares = 0
soma_total = 0
quantidade_total = 0

# Loop para a leitura dos números
while True:
    numero = int(input("Digite um número inteiro positivo (digite 0 para sair): "))
    
    # Verifica se o número é zero para encerrar a leitura
    if numero == 0:
        break
    
    # Verifica se o número é par ou ímpar e atualiza as variáveis correspondentes
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    
    soma_total += numero
    quantidade_total += 1

# Calcula a média dos valores pares
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0

# Calcula a média geral dos números lidos
if quantidade_total > 0:
    media_geral = soma_total / quantidade_total
else:
    media_geral = 0

# Exibe os resultados
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_total - quantidade_pares)
print("Média dos valores pares:", media_pares)
print("Média geral dos números lidos:", media_geral)
