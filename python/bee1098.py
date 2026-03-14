for i in range(0,21,2):
    I = i /10
    for j in range(1,4):
        J = I+j
        if i % 10 == 0:
            print(f"I={int(I)} J={int(J)}")
        else:
            print(f"I={I:.1f} J={J:.1f}")