Total_Doce = 0
Brigadeiro = 0
Beijinho = 0
Chocolate = 0

while True:
    Doce = input(" Qual Doce Ira comprar ?(Fim para sair): ")
    if Doce == "fim":
        break
    Quantidade = int(input(" Quantidade: "))
    if Doce.lower() == "Brigadeiro":
        Brigadeiro += Quantidade
    elif Doce.lower() == "Beijinho":
        Beijinho += Quantidade
    elif Doce.lower() == "Chocolate":
        Chocolate += Quantidade
    Total_Doce += Quantidade
    if Brigadeiro > 0:
        print(f" Foram comprados {Brigadeiro} Brigadeiros")
    if Beijinho > 0:
        print(f" Foram comprados {Beijinho} de beijinhos ")
    if Chocolate > 0:
        print(f" Foram comprados {Chocolate} de chocolates ")
print(f" O Total de doces comprados foram: {Total_Doce}")
