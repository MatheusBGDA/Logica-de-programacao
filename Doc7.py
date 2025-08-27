valor = float(input())

if 100 < valor:
    print('Fora do Intervalo')
elif 75 < valor:
    print("Intervalo (75,100]")
elif 50 < valor:
    print("Intervalo (50,75]")
elif 25 < valor:
    print("Intervalo (25,50]")
elif 0 < valor:
    print("Intervalo (0,25]")
else:
    print("Fora do Intervalo")