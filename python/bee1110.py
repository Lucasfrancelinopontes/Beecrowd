from collections import deque

while True:

    cartas = int(input())

    if cartas == 0:
        break

    pilha = deque(range(1, 1+ cartas))

    restante =[]
    if len(pilha) < 2:
        print("Discarded cards:")
        print("Remaining card: 1")
        continue

    while 2 <= len(pilha):
        remove = pilha.popleft()
        restante.append(remove)
        cartaBaixa = pilha.popleft()
        pilha.append(cartaBaixa)
    
    saida_formatada = ", ".join(map(str, restante))
    print(f"Discarded cards: {saida_formatada}")
              
    print("Remaining card:", pilha[0])



    