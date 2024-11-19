import grafico
import funcoes

areas = sorted([
  61, 65, 43, 53, 55, 51, 58, 55, 59, 56,
  52, 53, 62, 49, 68, 51, 50, 67, 62, 64,
  53, 56, 48, 50, 61, 44, 64, 53, 54, 55,
  48, 54, 57, 41, 54, 71, 57, 53, 46, 48,
  55, 46, 57, 54, 48, 63, 49, 55, 52, 51
])

menor_elemento = areas[0]

classes = []

for i in range(menor_elemento, areas[-1] + 1, 5):
  classes.append(i)

intervalos = []

for i in range(len(classes) - 1):
  intervalos.append([classes[i], classes[i + 1]])

intervalos[-1][1] = intervalos[-1][1] + 1

areas_sem_repetidos = list(set(areas))

areas_filtradas_com_fi = []

for intervalo in intervalos:
  result = ([areas.count(x) for x in areas_sem_repetidos if intervalo[0] <= x < intervalo[1]])
  areas_filtradas_com_fi.append([intervalo[0], intervalo[1], sum(result)])

###### ITEM 1 ######

# media
media = funcoes.media(areas_filtradas_com_fi)
# fim media

# moda
funcoes.moda(areas_filtradas_com_fi[1], areas_filtradas_com_fi[2], areas_filtradas_com_fi[3])
# fim moda

# mediana 
soma_total = funcoes.somatorio(areas_filtradas_com_fi)
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.5)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.5, "mediana")
# fim mediana

###### FIM DO ITEM 1 ######



###### ITEM 2 ######
funcoes.desvio_padrao(areas_filtradas_com_fi, media)
###### FIM DO ITEM 2 ######




###### ITEM 3 ######
# Q1
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.25)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.25, "Q1")
# FIM Q1

# D3
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.3)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.3, "D3")
# fim D3

# D7
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.7)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.7, "D7")
# fim D7

# P15
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.15)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.15, "P15")
# fim P15

# P90
posicao_ideal = funcoes.posicao_ideal(areas_filtradas_com_fi, soma_total, 0.9)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.9, "P90")
# fim P90

###### FIM DO ITEM 3 ######

###### ITEM 4 ######
grafico.monta_grafico(areas_filtradas_com_fi, 'frequência', 'classes')
###### FIM DO ITEM 4 ######