n = int(input())


contador_in = 0
contador_out = 0


for _ in range(n):
    x = int(input())
    
    
    if 10 <= x <= 20:
        
        contador_in += 1
    else:
        
        contador_out += 1


print(f"{contador_in} in")
print(f"{contador_out} out")