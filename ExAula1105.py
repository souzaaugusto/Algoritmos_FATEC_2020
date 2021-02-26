total_hoteis_15km = 0

acumulador_qtde_media_visitantes = 0.0
contador_qtde_media_visitantes = 0

while True:
  nome_hotel = input("Digite o nome do hotel: ")
  dist_hotel_centro = float(input("Digite a distancia do hotel ate o centro da cidade em km: "))
  nr_medio_visitantes = int(input("Numero medio de visitante no ultimo feriado: "))
  acesso_asfaltado = True if int(input("Tipo de asfalto (0 - Não asfaltado | 1 - Asfaltado")) == 1 else False

#Informação 01
  if dist_hotel_centro > 15:
    total_hoteis_15km += 1

#Informação 02
  if not acesso_asfaltado:
      contador_qtde_media_visitantes += 1
      acumulador_qtde_media_visitantes  += nr_medio_visitantes

#Informação 03
  if acesso_asfaltado and nr_medio_visitantes < 1000:
      print(nome_hotel, " - ", dist_hotel_centro)


  registrar_novo_hotel = input("Deseja registrar um novo hotel? (s|n): ")
  if registrar_novo_hotel.lower() == "n":
    break

print("Total de hotéis  fazenda cuja distancia está acima de 15km é igual a ", total_hoteis_15km)
print("Qtde  media de visitantes no ultimo feriado para hoteis com acesso não asfaltado é ", \
      0 if  contador_qtde_media_visitantes == 0 else (acumulador_qtde_media_visitantes / contador_qtde_media_visitantes))