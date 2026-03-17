valor = float(input())

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10 , 5, 1]

quantidade = 0

notasCentavos = int((valor * 100)+0.5)

print("NOTAS:")
for nota in notas:
    quantidade = notasCentavos // nota
    print(f"{quantidade} nota(s) de R$ {nota/100:.2f}")
    notasCentavos %= nota

print("MOEDAS:")
for moeda in moedas:
    quantidade = notasCentavos // moeda
    print(f"{quantidade} moeda(s) de R$ {moeda/100:.2f}")
    notasCentavos %= moeda
    