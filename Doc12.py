A, B = map(float, input().split(' '))

if A%B == 0 or B%A == 0:
    print("São multiplos")
else:
    print("Não são multiplos")