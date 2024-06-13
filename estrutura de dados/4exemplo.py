import os
os.system("cls || clear")

from dataclasses import dataclass

#Quantidade de vezes que pedira suas informações
QUANTIDADE_PETS = 2




# Classe.
@dataclass
class Pet:
    Nome: str
    Idade: int
    Raça: str
    Porte: str
    Alimentação:str


pets = []

#solicitando dados para o usuário.
for i in range(QUANTIDADE_PETS):
    pet = Pet(
        nome = input("\n Digite o titulo do livro: \n"),
        Idade  = input("Digite o nome do autor: \n"),
        Raça  = input("Digite a quantidade de páginas: \n"),
        Alimentação  = input("Digite o valor do livro: \n")
    )
    pets.append(pet)
     

    for i in livros:
        print(f"\ntitulo: {i.Nome}")
        print(f"Autor: {i.Idade}")
        print(f"Quantidade de páginas: {i.Raça}")
        print(f"Preço: {i.porte}")
