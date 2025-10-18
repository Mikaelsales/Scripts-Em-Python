total_vendas = 0
menor_vendas = None
maior_vendas = None
for i in range(1,8):
    Quantidade_vendida = int(input(""))
    total_vendas += Quantidade_vendida
    if maior_vendas is None or maior_vendas < Quantidade_vendida:
        maior_vendas = Quantidade_vendida
    if menor_vendas is None or menor_vendas > Quantidade_vendida:
        menor_vendas = Quantidade_vendida
media = total_vendas / 7
print(f"Sua media de vendas foi {media}")
print(f"O dia de maior vendas foi {maior_vendas}")
print(f"O dia de menor vendas foi {menor_vendas}")