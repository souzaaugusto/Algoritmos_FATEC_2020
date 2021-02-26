arquivo = open('dadosTeste.txt', encoding='utf-8')

content = arquivo.read().split('\n')
for line in content:
    print(line.strip())
#arquivo.seek(0,0)
#counter = 1
#for line in arquivo.readlines():
    #print(counter,' - ', line.strip())
    #counter += 1


arquivo.close()