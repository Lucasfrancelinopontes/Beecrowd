import math
casos = int(input())

for i in range(casos):
    valor1,valor2 = map(int,input().split())
    print(math.gcd(valor1,valor2))