while True:
    h1,m1,h2,m2 = map(int,input().split())
    if h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0:
        break
    h1,h2 = h1 *60, h2*60
    m1,m2 = h1 +m1, h2+m2
    if m2 <= m1:
        print((m2 + 1440) - m1)
    else:
        print(m2 - m1)
