import os

# Limpar terminal.
os.system("cls || clear")

# Inicializando variável.
resultado = "Dia útil"
dia_da_semana = ""

while True:
    os.system("cls || clear")

    # Solicitar dados para o usuário.
    ("Digite um número para o dia da semana: "))

    match(dia):
        case 1:
            dia_da_semana ="Picanha"
            
            break
        case 2:
            dia_da_semana ="Lasanha"
            break
        case 3:
            dia_da_semana ="Strogonoff"
            break
        case 4:
            dia_da_semana ="Bife Acebalodo"
            break
        case 5:
            dia_da_semana ="Pão com ovo"
            break
        case _:
            input("Código inválido!")
   
if resultado:
    print(f"Dia da semana: {dia_da_semana}")
    print(f"Resutado: {resultado}")