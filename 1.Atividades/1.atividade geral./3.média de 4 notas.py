import os 
os.system('cls || clear')

numero1 = int(input('Digite sua primeira nota:'))
numero2 = int(input('Digite sua segunda nota:'))
numero3 = int(input('Digite sua terceira  nota:'))
numero4 = int(input('Digite sua quarta nota:'))
os.system('cls || clear')

media = (numero1 + numero2 + numero3 + numero4)/4
print(f'---Resultado---')
print(f'primeiro: {numero1}')
print(f'segundo: {numero2}')
print(f'terceiro: {numero3}')
print(f'quarto: {numero4}')
print(f'media: {media}')