
salario = float(input())


imposto = 0.0

if salario <= 2000.00:
    
    imposto = 0.0
elif salario <= 3000.00:
    
    imposto = (salario - 2000.00) * 0.08
elif salario <= 4500.00:
    
    imposto = (1000.00 * 0.08) + (salario - 3000.00) * 0.18
else:
    
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + (salario - 4500.00) * 0.28


if imposto == 0.0:
    print("Isento")
else:
    
    print(f"R$ {imposto:.2f}")