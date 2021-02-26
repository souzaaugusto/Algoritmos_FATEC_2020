#Função recursiva de fatorial
def fat(n):
    if n == 0:
        return 1
    else:
        return  n * fat(n-1)
print(fat(6))

#Usando recursividade, calcule a soma de todos os valores de um vetor de números reais de 10 posições
#[0,1,2,3,4,5,6,7,8,9]
#0 + r[1:]
#1 + r[1:]()
#7 + r[1:](17)
#8 + r[1:] (9)
#if len(vet) == 1:
#    return vet[0]
#[9]
def soma_elem(v):
    if len(v) == 1:
        return v[0]
    else:
        return v[0] + soma_elem(v[1:])

items = [23.0, 45.0, 67.5, 89.0, 98.0, 12.1, 222.2, 398.6, 0.67, 10.56]
result = soma_elem(items)
print(result)
