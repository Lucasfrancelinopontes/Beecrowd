casos = int(input())
pares =[]
impares = []

for i in range(casos):

    valor = int(input())
    if valor %2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort()
impares.sort(reverse=True)

for i in pares:
    print(i)
for i in impares:
    print(i)