import os 
os.system('cls || clear')
media = input
nome = str(input('Digite seu nome'))
nota1 = int(input('Digite a primeira nota'))
nota2 = int(input('Digite a segunda nota'))

media = (nota1 + nota2)/2

print(f'Nome: {nome}')
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'media : {media}')