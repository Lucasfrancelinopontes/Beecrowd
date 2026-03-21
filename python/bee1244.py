casos = int(input())

for i in range(casos):
    frase = input().split()
    fraseOrdenada = sorted(frase,key=len,reverse=True)
    
    resultado = " ".join(fraseOrdenada)

    print(resultado)
    