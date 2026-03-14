tempo = int(input())

horas = tempo // 3600
tempo = tempo % 3600
minutos = tempo // 60
tempo = tempo % 60
segundos = tempo

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")
