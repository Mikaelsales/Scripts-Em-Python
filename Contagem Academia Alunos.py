Total_Alunos_Treino = int(input(" Quantas Pessoas Irão Treinar Hoje?: "))
Numero_para_Tirar_Media = 0
Nomes = []
Minutos_Total = 0
Exercicios_Total_Feitos = 0
Mais_Treinou = None
Menos_Treinou = None
Nome_Maior_Treino = ""
Nome_Menor_Treino = ""
while True:
     Nome = input("Seu Nome: ")
     Nomes.append(Nome)

     Tempo_Treino = int(input("Tempo De Treino(Em Minutos): "))
     Minutos_Total += Tempo_Treino

     Exercicios_Feitos = int(input("Quantos Exercicios Feitos: "))
     Exercicios_Total_Feitos += Exercicios_Feitos
     Total_Alunos_Treino -= 1
     Numero_para_Tirar_Media += 1
     if Mais_Treinou is None or Tempo_Treino > Mais_Treinou:
          Mais_Treinou = Tempo_Treino
          Nome_Maior_Treino = Nome
     if Menos_Treinou is None or Tempo_Treino < Menos_Treinou:
          Menos_Treinou = Tempo_Treino
          Nome_Menor_Treino = Nome
     
     
     if Total_Alunos_Treino == 0:
          break
          
Media_Exercicios_Total = Exercicios_Total_Feitos / Numero_para_Tirar_Media
