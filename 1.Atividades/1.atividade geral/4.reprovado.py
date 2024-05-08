import os 
os.system('cls || clear')

numero1 = int(input('Digite sua primeira nota:'))
numero2 = int(input('Digite sua segunda nota:'))
numero3 = int(input('Digite sua terceira  nota:'))

media = (numero1 + numero2 + numero3) / 3

if media >= 7:
    print("Passou de ano!!")
else:
    print("Reprovado")

print(f'---Resultado---')
print(f'primeiro: {numero1}')
print(f'segundo: {numero2}')
print(f'terceiro: {numero3}')
print(f'Média: {media}')
