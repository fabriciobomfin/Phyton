import os

# Função sem retorno retorno.
def logoSenai():
    os.system("cls || clear") #Apagar terminal
    print(" == == == === == ==")
    print(" SENAI DENDENZEIRAS ")
    print(" == == == === == ==")

# Função com retorno retorno.
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def subitrair(p1, p2):
    resultado = p1 - p2
    return resultado

def multiplicar(p1, p2):
    resultado = p1 * p2
    return resultado

def dividir(p1, p2):
    resultado = p1 / p2
    return resultado
 
#Solicitando dados para o úsuario.
logoSenai()
primeiroNumero = int(input("Digite o primeiro número:\n"))

logoSenai()
segundoNumero = int(input("Seu segundo número:\n"))



resultado1 = somar(primeiroNumero,segundoNumero)
resultado2 = subitrair(primeiroNumero,segundoNumero)
resultado3 = multiplicar(primeiroNumero,segundoNumero)
resultado4 = dividir(primeiroNumero,segundoNumero)

#Exibindo dados para o usuário
logoSenai()
print(f"Soma: {resultado1}")
print(f"Subtrair: {resultado2}")
print(f"Multiplicar: {resultado3}")
print(f"Dividir: {resultado4}")
