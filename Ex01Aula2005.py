import random as r

def epar(numero):
    return numero % 2 == 0

def elementos_lista_epar(lista_numeros):
    resultado = []
    for numero in lista_numeros:
        resultado.append(epar(numero))
        return resultado
    #return [ epar(numero) for numero in lista_numeros]
print("{0}, {1}".format(epar(3), epar(2)))

lista= [r.randint(2,1675) for i in range(0,100)]
print(lista)
for i in range(0,4):
    print(r.choice(lista))

str_to_list = list('ole ole ola')
r.shuffle(str_to_list)
print(str_to_list)
print(''.join(str_to_list))

#print(elementos_lista_epar(lista))

#def muda_e_imprime(a):
 #   a = 7
  #  print(a)
   # return a
#a=5
#a=muda_e_imprime(a)

#exercicios da lista 7:
# 1 returnlen(nums) > 0 and (nums[0] == 6 or nums[-1] == 6)
# 2 returnlen(nums) > 0 and (nums[0] == [-1])