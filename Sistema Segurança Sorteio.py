## Sistema de segurança BASICO, Para entrada em Sorteio
print(' Olá, Bote Suas Informações!! ')
Nome = input(' Nome: ')
Idade = int(input(' Idade: '))
Data_Nascimento = int(input('Data Nascimento: '))
Numero_Telefonico = int(input(' Numeros Celular: '))
while True:
    if Idade <= 17:
        print(" Novo Demais!! ")
        break
    if Idade >= 18:
        print(" Prossiga!! ")
Numero_Cartão = int(input(" Numeros Cartão: "))
print(" Obrigado!! Já Está No Sorteio! ")