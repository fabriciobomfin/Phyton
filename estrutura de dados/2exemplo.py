import os
os.system("cls || clear")

from dataclasses import dataclass


QUANTIDADE_ALUNOS = 2


# Classe.
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float


alunos = []

#solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    
    
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        altura = float(input("Digite sua altura: ")),
        peso = float(input("Digite seu peso: "))
    ) #sempre colocar virgulas em todos antes do ultimo
    alunos.append(aluno)
     
    #Imprimindo as informações do usuario
    for i in alunos:
        print(f"Nome: {i.nome}")
        print(f"Idade: {i.idade}")
        print(f"Altura: {i.altura}")
        print(f"peso: {i.peso}")
    
