casos = int(input())

for i in range(casos):
    frase = input()
    posicao = int(input())

    codificada = ""

    for j in frase:
        if ord(j) - posicao < 65:
            codificada = codificada + chr((ord(j) - posicao) + 26)
        else:
            codificada = codificada + chr(ord(j) - posicao)

    print(codificada)