chaCerto = input()
avaliacoes = input()
ct = 0
total = 0
chaAtual = 0

while True:
    chaAtual = avaliacoes.find(chaCerto,chaAtual + ct)
    ct = 0
    if chaAtual != -1:
        total += 1
    else:
        break
    ct = 1
print(total)