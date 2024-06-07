import os

# Limpar terminal.
os.system("cls || clear")

def cab ():
    os.system ("cls || clear")

opcao = int (input (" 1 = pagamento a vista  e  2 = pagamento a prazo: \n => "))
valor = int (input ("valor do produto: \n ==> "))

cab ()
match(opcao):
    case 1:
        desconto = valor * 0.10
        resultado = valor - desconto
        print (f"forma de pagamento- á vista")
        print (f"valor do produto: {valor}")
        print (f"valor do desconto: {desconto}")
        print (f"valor do produto: {resultado}")
    case 2:
        parcela = int (input("quantidade de parcela ? \n ==> "))
        os.system ("cls || clear")
        valorParcela = valor / parcela
        print ("valor R$ - 100")
        print (f"forma de pagamento: á prazo")
        print (f"valor total a prazo : {valor}")
        print (f"quantidade de parcela: {parcela}")
        print (f"valor da parcela: {valorParcela}")