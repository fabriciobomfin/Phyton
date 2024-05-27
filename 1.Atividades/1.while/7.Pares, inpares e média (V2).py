import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicializando as variáveis
soma_pares = quantidade_pares = soma_total = quantidade_total = 0

# Loop para a leitura dos números
while True:
    clear_screen()
    numero = int(input("Digite um número inteiro positivo (digite 0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    soma_total += numero
    quantidade_total += 1

# Calcula a média dos valores pares
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0

# Calcula a média geral dos números lidos
media_geral = soma_total / quantidade_total if quantidade_total > 0 else 0

# Exibe os resultados
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_total - quantidade_pares)
print("Média dos valores pares:", media_pares)
print("Média geral dos números lidos:", media_geral)
