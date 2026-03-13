valor1, valor2, valor3 = map(int,input().split())

if (valor1 >= valor2) and (valor1 >= valor3):
    print(f"{valor1} eh o maior")
elif (valor2 >= valor1) and (valor2 >= valor3):
    print(f"{valor2} eh o maior")
elif (valor3 >= valor2) and (valor3 >= valor1):
    print(f"{valor3} eh o maior")