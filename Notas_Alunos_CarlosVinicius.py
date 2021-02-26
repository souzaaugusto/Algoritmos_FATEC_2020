#LEITURA DO ARQUIVO FONTE E SEPARAÇÃO DA PONTUAÇÃO:
arquivo = open('dados.txt')
estudantes = []
dic = {}
notasFinais = []
for linha in arquivo.readlines():
        line = linha.strip('\n')
        x = line.split(':')
        if x[0] == '#':
            x[0] = ','
            estudantes.append(dic)
            dic = {}
        else:
            dic[x[0]] = x[1]
#print(estudantes)

#FUNÇÃO PARA EXIBIR OS DETALHES DO DICIONÁRIO:
def detail():
    for dados in estudantes:
        print('Nome:', dados['nome'])
        print('Notas Deveres:', dados['deveres'])
        print('Notas quizzes:', dados['quizzes'])
        print('Notas Testes:', dados['testes'])
        print('-----------------------------------')
#print(detail())

#FUNÇÃO PARA CALCULAR A MÉDIA SIMPLES DE QUALQUER VALOR SOLICITADO:
def media_simples(notas):
    total = 0
    contagem = 0
    for n in notas:
        total += n
        contagem += 1
    media = round(total / contagem, 2)
    print('A média geral da classe é: ', media)
#print(media_simples([10,20,30,40]))

#FUNÇÃO PARA MOSTRAR AS MEDIAS PONDERADAS DAS NOTAS DOS ALUNOS:
def getAverage(aluno):
    notaDeveres = aluno['deveres'].split(',')
    mediaDeveres = sum([float(i) for i in notaDeveres]) / len(notaDeveres) * 0.1
    notaQuizzes = aluno['quizzes'].split(',')
    mediaQuizzes = sum([float(i) for i in notaQuizzes]) / len(notaQuizzes) * 0.3
    notaTestes = aluno['testes'].split(',')
    mediaTestes = sum([float(i) for i in notaTestes]) / len(notaTestes) * 0.6
    mediaPonderada = round(mediaDeveres + mediaQuizzes + mediaTestes, 2)
    #print('\nA média ponderada de', aluno['nome'], 'é:', mediaPonderada)
    return mediaPonderada

#FUNÇÃO PARA MOSTRAR O CONCEITO DA MEDIA PONDERADA DOS ALUNOS:
def getLetterGrade(pontuacao):
    if pontuacao >= 90:
        print('Seu conceito foi: A')
    elif pontuacao >= 80 and pontuacao :
        print('Seu conceito foi: B')
    elif pontuacao >= 70 and pontuacao < 80:
        print('Seu conceito foi: C')
    elif pontuacao >= 60 and pontuacao < 70:
        print('Seu conceito foi: D')
    else:
        print('Seu conceito foi: F')
#print(getLetterGrade(80))

#FUNÇÃO PARA MOSTRAR A MÉDIA PONDERADA INDIVIDUAL DO ALUNO:
def alunoNotaIndividual():
    try:
        nome = input('Digite o nome do aluno para ver sua média individual:')
        print(nome)
        for dados in estudantes:
            if dados['nome'] == nome:
                print('A média ponderada de ', dados['nome'], ' é: ', getAverage(dados))
    except ValueError:
        print('Aluno não cadastrado')
#print(alunoNotaIndividual())

#CALCULO FINAL PARA DEMONSTRAR TODAS AS FUNÇÕES:
def getClassAverage():
    print('=============DETAIL==============')
    detail()
    print('==========MÉDIAS PONDERADAS=========')
    for dados in estudantes:
        print('A média ponderada de', dados['nome'], 'é:', getAverage(dados))
        getLetterGrade(getAverage(dados))
        print('-------------------------------------')
        notasFinais.append(getAverage(dados))
    print('==========MÉDIA FINAL TURMA==========')
    media_simples(notasFinais)
print(getClassAverage())
arquivo.close()



