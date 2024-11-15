import math
import funcoes

areas = [
    [300, 400, 14],
    [400, 500, 46],
    [500, 600, 58],
    [600, 700, 76],
    [700, 800, 68],
    [800, 900, 62],
    [900, 1000, 48],
    [1000, 1100, 22],
    [1100, 1200, 6]
]


###### ITEM 1 ######

# media
media = funcoes.media(areas)
# fim media

# moda
funcoes.moda(areas[2], areas[3], areas[4])
# fim moda

# mediana 
soma_total = funcoes.somatorio(areas)
posicao_ideal = funcoes.posicao_ideal(areas, soma_total, 0.5)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.5, "MEDIANA")
# fim mediana

###### FIM DO ITEM 1 ######



###### ITEM 2 ######
funcoes.desvio_padrao(areas, media)
###### FIM DO ITEM 2 ######




###### ITEM 3 ######
# Q1
posicao_ideal = funcoes.posicao_ideal(areas, soma_total, 0.25)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.25, "Q1")
# FIM Q1

# D3
posicao_ideal = funcoes.posicao_ideal(areas, soma_total, 0.3)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.3, "D3")
# fim D3

# D7
posicao_ideal = funcoes.posicao_ideal(areas, soma_total, 0.7)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.7, "D7")
# fim D7

# D7
posicao_ideal = funcoes.posicao_ideal(areas, soma_total, 0.15)
funcoes.encontra_medidas(posicao_ideal, soma_total, 0.15, "P15")
# fim D7

###### FIM DO ITEM 3 ######