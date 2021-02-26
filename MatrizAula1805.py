import random as r

matriz = []
DIMENSAO = 4
for i in range(0, DIMENSAO):
    linha = []
    for j in range(0, DIMENSAO):
        linha.append(r.randint(-99, 99))
    matriz.append(linha)
print(matriz)

#elementos da diagonal principal
for i in range(0, DIMENSAO):
    for j in range(0, DIMENSAO):
        if i == j:
            print(matriz[i][j])

#elemtos diferentes da diagonal principal
print(matriz)
for i in range(0, DIMENSAO):
    for j in range (0, DIMENSAO):
        if i != j:
            print(matriz[i][j])

#elementos diagonal secundaria
print(matriz)
for i in range(0, DIMENSAO, 1):
    for j in range ((DIMENSAO -1), -1,-1):
        if(i+j) == (DIMENSAO -1):
            print(matriz[i][j])