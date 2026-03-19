par =0
impar =0
positivo =0
negativo =0

for i in range(5):
    pega = int(input())

    if pega != 0:
        if pega%2 == 0:
            par +=1
        else:
            impar += 1
        if pega > 0:
            positivo +=1
        else:
            negativo +=1
    else:
        par+= 1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")