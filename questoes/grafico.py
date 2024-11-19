import matplotlib.pyplot as plt

def split_matriz(matrix):
  areas = []
  lotes = []
  for linha in matrix:
    areas.append(f"{linha[0]} |- {linha[1]}")
    lotes.append(linha[2])
  return [areas, lotes]


def monta_grafico(areas, nome_lateral, nome_inferior):
  dados = split_matriz(areas)
  linhas = dados[0]
  colunas = dados[1]
  plt.bar(linhas, colunas)
  plt.title('Gráfico de Barras')
  plt.xlabel(nome_inferior)
  plt.ylabel(nome_lateral)
  plt.show()
