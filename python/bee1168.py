stop = int(input())

tabela_leds = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

for i in range(stop):
    total = 0
    numero = input()
    
    for j in numero:
        total += tabela_leds[j]
    print(f"{total} leds")
    