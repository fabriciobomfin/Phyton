import os
os.system("cls || clear")

from dataclasses import dataclass

#Quantidade de vezes que pedira suas informações
QUANTIDADE_LIVROS = 2

# Classe.
@dataclass
class Livro:
    titulo: str
    autor: str
    paginas: int
    preço: float


livros = []

#solicitando dados para o usuário.
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        titulo = input("\n Digite o titulo do livro: \n"),
        autor = input("Digite o nome do autor: \n"),
        paginas = input("Digite a quantidade de páginas: \n"),
        preço = input("Digite o valor do livro: \n")
    )
    livros.append(livro)
     

    for i in livros:
        print(f"\ntitulo: {i.titulo}")
        print(f"Autor: {i.autor}")
        print(f"Quantidade de páginas: {i.paginas}")
        print(f"Preço: {i.preço}")
