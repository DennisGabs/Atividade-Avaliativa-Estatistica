import math

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


def desvio_padrao(areas, media):
    variancia = 0
    k = 0 
    for area in areas:
        ponto_medio = (area[0] + area[1]) / 2
        variancia += ( ( ponto_medio - media ) ** 2 ) * area[2]
        k += area[2]

    variancia = variancia / ( k - 1 )
    print('desvio padrão =', round(math.sqrt(variancia), 2))


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

## responsável por encontrar a mediana, Q1, D3...
def encontra_medidas(linha, soma_total, percentual, medida):
    valor_temp = soma_total * percentual
    h = (linha[1] - linha[0])
    valor = linha[0] + (valor_temp - linha[-1]) / linha[2] * h
    print(medida, "=", round(valor, 2))

## Encontra a linha ideal na matriz de areas dado o percentual
def posicao_ideal(areas, somatorio_total, percentual):
    aux = 0
    limite = somatorio_total * percentual
    ultima_pos = areas[0]
    pos = 0
    for area in areas:
        aux += area[2]
        ultima_pos = area
        if aux >= limite:
            ultima_pos.append(aux - area[2])
            break
    return ultima_pos