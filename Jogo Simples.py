import random
nome_jogador = input(" Digite seu nome: ")
Numero_secreto = random.randint(1,10)
tentativas = 5

while tentativas > 0:
    Resposta = int(input(" Diga seu numero: "))
    if Resposta == Numero_secreto:
        print(f"{nome_jogador}, Você ganhou!! ")
        break
    elif Resposta > Numero_secreto:
        print(f"{nome_jogador}, Alto demais!! ")
    else:
        print(f"{nome_jogador}, Baixo demais!!")
    tentativas -= 1
    print(f"{nome_jogador}, Suas Tentativas Restante:{tentativas}  ")
if tentativas == 0:
    print(f" Você perdeu {nome_jogador}!! ")