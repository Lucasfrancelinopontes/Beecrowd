h1,h2 = map(int,input().split())

inicio,fim = h1,h2

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")
else:
    if fim >= inicio:
        totalH = (fim - inicio) 

        print(f"O JOGO DUROU {totalH} HORA(S)")
    else:
        totalH = ((fim - inicio) +24) 
        print(f"O JOGO DUROU {totalH} HORA(S)")