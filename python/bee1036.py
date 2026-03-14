a,b,c = map(float,input().split())

delta = (b**2) - (4*a*c)

if delta >= 0:
    if a > 0:
        bashkara1 = ((b - (b*2)) + (delta ** 0.5))/ (2*a)
        bashkara2 = ((b - (b*2)) - (delta ** 0.5))/ (2*a)
        print(f"R1 = {bashkara1:.5f}")
        print(f"R2 = {bashkara2:.5f}")
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")