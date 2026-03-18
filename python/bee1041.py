x,y = map(float,input().split())

if x != 0 or y != 0:
    if x == 0:
        print("Eixo Y")
    elif y == 0:
        print("Eixo X")
    else:
        if x > 0:
            if y > 0:
                print("Q1")
            else:
                print("Q4")
        else:
            if y > 0:
                print("Q2")
            else:
                print("Q3")
else:
    print("Origem")
    