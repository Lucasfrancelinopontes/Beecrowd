codigo, qtd = map(int,input().split())

lanches = [4.00,4.50,5.00,2.00,1.50]

total = lanches[codigo -1] * qtd

print(f"Total: R$ {total:.2f}")