## Comando isalpha Faz com que apenas Letras Sejam Aceitas


print(" Olá, seja bem vindo! Qual seu nome ?")
Nome_usuario = input("")
print(f" Ok Qual será seu pedido {Nome_usuario}? ")
Contador = 0
Lista = []
while True:
    Pedido = input("Seu Pedido: ")
    if Pedido == "sair":
        break
    elif Pedido.isalpha():
        Lista.append(Pedido)
        Contador += 1
        print(Lista)
    else:
        print("Erro, Digite Apenas Letras!! ")
print(f"Total De Pedidos Foram {Contador}, {Nome_usuario}.")  