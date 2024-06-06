import os 
os.system('cls || clear')

# Inicializando variável.
resultado = False

# Solicitar dados para o usuário.
a = int(input("Digite o primeiro número: "))
operador = input("Digite o operador: (+, -, *, / ): ")
b = int(input("Digite o segundo número: "))


match(operador):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case'*':
        resultado = a * b
    case '/':
        resultado = a / b
    case _:
        print("Operador inválido")
    
    

if resultado:
    print(f"Resultado: {resultado}")