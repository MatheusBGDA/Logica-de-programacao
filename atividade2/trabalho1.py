contador_pares = 0


for _ in range(5):
    numero = int(input())
    
    
    if numero % 2 == 0:
        
        contador_pares += 1


print(f"{contador_pares} valores pares")