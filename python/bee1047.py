h1,m1,h2,m2 = map(int,input().split())

inicio,fim = (h1*60) + m1,(h2*60)+m2

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if fim >= inicio:
        totalH = (fim - inicio) // 60
        totalM = (fim - inicio) % 60

        print(f"O JOGO DUROU {totalH} HORA(S) E {totalM} MINUTO(S)")
    else:
        totalH = ((fim - inicio) +1440) // 60
        totalM = ((fim - inicio) + 1440) % 60

        print(f"O JOGO DUROU {totalH} HORA(S) E {totalM} MINUTO(S)")