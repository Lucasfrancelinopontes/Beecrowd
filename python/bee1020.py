idade = int(input())

ano = idade // 365
idade = idade % 365
mes = idade // 30
idade = idade % 30
dia = idade

print(f"{ano:.0f} ano(s)")
print(f"{mes:.0f} mes(es)")
print(f"{dia:.0f} dia(s)")