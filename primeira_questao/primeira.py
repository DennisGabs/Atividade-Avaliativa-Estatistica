import math

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

def media(areas):
    media = 0
    ponto_medio = 0
    k = 0 
    for area in areas:
        ponto_medio = (area[0] + area[1])/2
        media += ponto_medio * area[2]
        k += area[2]

    media = media / k

    print('média =', media)
    return media

def moda(anterior, moda, posterior):
    moda = moda[0] + (posterior[2] / (posterior[2] + anterior[2])) * (moda[1] - moda[0])
    print('moda =', round(moda, 2))

def mediana(frequencias, metade_total, frequencia_anterior):
    h = (frequencias[-1][1] - frequencias[-1][0])
    mediana = frequencias[-1][0] + (( metade_total - frequencia_ant ) / frequencias[-1][2]) * h
    print('mediana =', round(mediana, 2))

def somatorio(areas):
    soma_total = 0
    for area in areas:
        soma_total += area[2]
    return soma_total


def frequencia_anterior(areas, posicao_limite):
    somatorio_frequencia = 0
    for i in range(posicao_limite):
        somatorio_frequencia += areas[i][2]
    return somatorio_frequencia



## item 1

## MEDIA
media = media(areas)
## FIM MEDIA

## MODA
moda(areas[2], areas[3], areas[4])
## FIM MODA

## MEDIANA 
soma_total = somatorio(areas)
metade_total = soma_total / 2
frequencia_ant = frequencia_anterior(areas, 4)
mediana([areas[0], areas[1], areas[2], areas[3], areas[4]], metade_total, frequencia_ant)
## FIM MEDIANA

## fim do item 1

## item 2
def desvio_padrao(areas, media):
    variancia = 0
    k = 0 
    for area in areas:
        ponto_medio = (area[0] + area[1]) / 2
        variancia += ( ( ponto_medio - media ) ** 2 ) * area[2]
        k += area[2]

    variancia = variancia / ( k - 1 )
    print('desvio padrão =', round(math.sqrt(variancia), 2))


desvio_padrao(areas, media)
## fim do item 2


## item 3
def q1(area, soma_total, frequencia_anterior):
    valor_temp = soma_total * 0.25
    q1 = area[0] + (valor_temp - frequencia_anterior) / area[2] * (area[1] - area[0])
