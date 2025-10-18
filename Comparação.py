Nome = input(" Seu nome: ")
Idade = int(input(" Sua idade: "))

if Idade >=18:
    print(f"{Nome}, idade Permitida")
else:
    print(f"{Nome}, idade Não Permitida")



Minha_Musica = " R.U Mine "
Sua_Musica = input(" Bote Sua Musica: ")

if Minha_Musica == Sua_Musica:
    print(" Nossas Musicas São Iguais!!")
else:
    print( " Nossas Musicas Não São Iguais :C ")



Minha_Pontuação = 1300
Nome_Amigo = input(" Seu Nome: ")
Pontuação_Amigo = int(input("Sua pontuação: "))

if Minha_Pontuação > Pontuação_Amigo:
    print(f"{Nome_Amigo}, Minha pontuação e maior!!")
elif Minha_Pontuação < Pontuação_Amigo:
    print(f"{Nome_Amigo}, Minha pontuação e menor!!")
else:
    print(" Pontuação iguais!! ")



Voce_Concorda_Com_Essa_Afirmação = print(" Python e mior que buseta")
Sim_Não = input(" Voce concorda?: ")

if  Sim_Não == "Sim":
    print(" Parabéns você e esperto")
else:
    print(" burro ")