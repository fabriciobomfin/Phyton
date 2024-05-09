import os
#Limpar o terminal 
import os 

os.system('cls || clear')

# Variáveis para armazenar os dados
idades = []
salarios = []
quantidade_mulheres_salario_maior_5000 = 0
1

# Loop principal do código
while True:
    print("\nMenu:")
    print("1. Adicionar pessoa")
    print("2. Exibir resultados e sair")
    codigo = int(input("Digite o código da opção desejada: "))
    
    if codigo == 1:
        idade = int(input("Digite a idade da pessoa: "))
        idades.append(idade)
        salario = float(input("Digite o salário da pessoa: "))
        salarios.append(salario)
        sexo = input("Digite o sexo da pessoa (M/F): ")
        if sexo.upper() == 'F' and salario >= 5000:
            quantidade_mulheres_salario_maior_5000 += 1
    elif codigo == 2:
        # Verificando se há dados para calcular
        if idades:
            media_salario = sum(salarios) / len(salarios)
            maior_idade = max(idades)
            menor_idade = min(idades)
            print("\nResultados:")
            print(f"Média de salário do grupo: R${media_salario:.2f}")
            print(f"Maior idade do grupo: {maior_idade} anos")
            print(f"Menor idade do grupo: {menor_idade} anos")
            print(f"Quantidade de mulheres com salário maior ou igual a R$ 5.000,00: {quantidade_mulheres_salario_maior_5000}")
        else:
            print("Não há dados para exibir.")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

