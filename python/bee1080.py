maior = 0
posicao = 0
x = 0
while x < 100:
    numero = int(input())
    if numero > maior:
        maior = numero
        posicao = x+1
    x += 1
    
print(maior)
print(posicao)