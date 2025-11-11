import random
import time
senha_str = input("Senha: ")
senha_transformar_int = int(senha_str)
Tamanho_senha = int(input(" Tamanho Dela: "))
Senha_achada = False
Quantas_Tentativas_necessarias = 0

while not Senha_achada:
    Tentativas_int = random.randint(1,(10**Tamanho_senha)- 1)
    print(Tentativas_int)
    tentativas_str = str(Tentativas_int)
    Quantas_Tentativas_necessarias += 1
    if Tentativas_int == senha_transformar_int:
        Senha_achada = True
        break
print(f" Achada: {Senha_achada}")
print(f" Tentativas: {Quantas_Tentativas_necessarias}")
