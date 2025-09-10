def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida"

# Entrada do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")

# Cálculo e saída
resultado = calcular(n1, n2, op)
print("Resultado:", resultado)