medias = []
for index in range(0, 10):
    nota1 = float(input("Informe a nota 1: "))
    nota2 = float(input("Informe a nota 2 : "))
    nota3 = float(input("Informe a nota 3: "))
    nota4 = float(input("Informe a nota 4: "))

    media = (nota1+nota2+nota3+nota4)/4

    medias.append(media)

    for media in medias:
        if media >= 7.0:
            print(media)