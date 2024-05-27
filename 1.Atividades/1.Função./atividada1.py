#crie uma função que receba 2 números, mostre uma mensagem com a média destes dois números
import os

# Função sem retorno retorno.
def logoSenai():
    os.system("cls || clear") #Apagar terminal
    print(" == == == === == ==")
    print(" SENAI DENDENZEIRAS ")
    print(" == == == === == ==")

# Função com retorno retorno.
def calcular_media(n1, n2, n3):
    resultado = (n1 + n2 + n3) / 3
    return resultado


#Solicitando dados para o úsuario.
logoSenai()
primeiroNumero = int(input("Digite o primeiro número:\n"))

logoSenai()
segundoNumero = int(input("Digite o segundo número:\n"))

logoSenai()
terceiroNumero = int(input("Digite o terceiro número:\n"))


resultado1 = calcular_media(primeiroNumero,segundoNumero,terceiroNumero)


#Exibindo dados para o usuário
logoSenai()
print(f"Média: {resultado1}")
