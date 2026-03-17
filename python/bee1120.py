while True:
    valorErrado, valor = input().split()

    if valorErrado == "0" and valor == "0":
        break

    valorCorrigido = ''

    for numero in valor:
        if numero != valorErrado:
            valorCorrigido = valorCorrigido + numero

    if valorCorrigido:
        print(int(valorCorrigido))
    else:
        print(0)
        