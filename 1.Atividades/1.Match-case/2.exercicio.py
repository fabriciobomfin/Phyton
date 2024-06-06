#Desenvolva um pograma que receba como entrada um número inteiro que represente um dos 7 dias da semana e imprima na tela se esse dia é útil, final de semana ou inválido.
#considere Domingo o dia 1 e sabado o dia 7

import os 
os.system('cls || clear')

resultado = False

semana = int(input("Digite um número entre 1 e 7: "))
      
match(semana):
    case 1:
        resultado = "Domingo"
    case 2:
        resultado = "Segunda"
    case 3:
        resultado = "Terça"
    case 4:
        resultado = "Quarta"
    case 5:
        resultado = "Quinta"
    case 6:
        resultado = "Sexta"
    case 7:
        resultado = "Sabado"
    case _:
        print("Digito inválido.")
        
if resultado:
    print(f"Resultado: {resultado}")    