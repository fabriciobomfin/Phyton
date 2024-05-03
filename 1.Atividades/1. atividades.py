import os 
os.system('cls || clear')

print("\n== Solicitando dados ===")
pesoMorangos = input("Digite o peso de morangos (em kg):  ")
pesoMacas = input ("Digite o peso de maçãs (em kg): ")

if pesoMorangos > 5:
    precoMorango = 2.50
else :
    precoMorango = 2.20

if pesoMarcas < 5 :
    precoMaca = 1.80
else:
    precoMaca = 1.50

pesototal = pesoMorangos + pesoMacas 
subtotal = (precoMorango * pesoMorangos) + (precoMaca * pesoMacas)

if pesoTotal > 8 or subtotal > 25:
    desconto = subtotal * 0.10

totalPagar = subtotal - desconto

print(f"peso de morangos (em Kg): ")