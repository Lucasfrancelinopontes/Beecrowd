while True:
    parentesesE = 0
    parentesesD = 0
    erro = 0
    try:
        expressao = input()

        for elemento in expressao:
            if elemento == ")":
                parentesesE += 1
            if elemento == "(":
                parentesesD += 1
            if parentesesE > parentesesD:
                erro = 1
                break
        if parentesesD == parentesesE and erro == 0:
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break