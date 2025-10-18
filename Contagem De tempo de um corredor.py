mais_rapido = None
mais_lento = None
total_tempo = 0

for i in range(1,6):
    tempo = int(input(""))
    total_tempo += tempo
    if mais_rapido is None or mais_rapido > tempo:
        mais_rapido = tempo
    if mais_lento is None or mais_lento < tempo:
        mais_lento = tempo
media = total_tempo / 5
print(f" A media de tempo foi {media}")
print(f" O mais rapido foi {mais_rapido}")
print(f" O mais lento foi {mais_lento}")