numeros = list(map(int, input().split(' ')))

auxNumeros = list(numeros)

numeros.sort()

for n in numeros:
    print(n)

print()
#o print vazio é para deixar uma linha em branco
for n in auxNumeros:
    print(n)