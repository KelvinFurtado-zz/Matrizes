#Dado um número N e respectivos valores
#Monta uma matriz Quadrada NxN
def criaMatrizQuad():
  lin = int(input("Insira o valor N da dimensão da matriz quadrada NxN: "))

  matriz = []
  for i in range(lin):
    linha = []
    for j in range(lin):
      x = float(input("Insira o valor da {}º linha e {}º coluna da matriz: ".format(i+1,j+1)))
      linha.append(x)
    matriz.append(linha)
  for i in matriz:
    print(i)
  return matriz

#Calcula o determinante de uma matriz de ordem 4 ou maior
# Usando o Teorema de Laplace
# Escolhe-se uma fila (linha ou coluna) qualquer, nesse caso será escolhida a primeira linha
#Determinante é igual a soma de cada valor dessa fila multiplicado pelo seu cofator
def determinanteLaplace(matriz):
  det = 0
  for i in range(len(matriz)):
    det += matriz[0][i] * cofator(0,i,matriz)
  return det

# O menor complementar de um elemento de uma matriz quadrada 
# É o determinante da matriz retirando os elementos de mesma linha e coluna desse elemento

def menorComplementar(lin, col, matriz):
  matrizAux = []
  for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz)):
      if i != lin and j != col:
        linha.append(matriz[i][j])
    if linha != []:
      matrizAux.append(linha)
  return determinante(matrizAux)

# Cij = (-1)**(i+j) x Dij (Dij => Menor complementar)
def cofator(lin,col,matriz):
  return (-1)**(lin+col) * menorComplementar(lin,col, matriz)

#Calcula Determinante de uma matriz quadrada
def determinante(matriz):
  if len(matriz) > 0:
    if len(matriz) == 1:
      return matriz[0]
    elif len(matriz) == 2:
      return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
      return determinanteLaplace(matriz)
  else:
    print("Tamanho da matriz precisa ser maior que zero!")


print("O determinante da matriz é: {}".format(determinante(criaMatrizQuad())))
input("Aperte Enter para finalizar...")