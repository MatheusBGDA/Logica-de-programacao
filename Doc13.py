lados = input().split()

A, B, C = sorted(map(float, lados), reverse=True)

if A >= (B + C):
    print("Não forma triângulo")
else:
    if (A*A) == ((B*B) + (C*C)):
        print("Triângulo retângulo")
    elif (A*A) > (B*B) + (C*C):
        print("Triângulo Obtusangulo")
    elif (A*A) < (B*B) + (C*C):
        print("Triângulo Acutangulo")
lados = [A, B, C]

if lados.count(A) == 2 or lados.count(B) == 2:
    print("Triângulo Isosceles")
if lados.count(A) == 3:
    print("Triângulo Equilatero")