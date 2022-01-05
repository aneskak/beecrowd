#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o 
# código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor 
# a ser pago.
#
#Entrada
#O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois 
# inteiros e um valor com 2 casas decimais.
#
#Saída
#A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os 
# dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.


C1, N1, V1 = input().split()
C1 = int(C1)
N1 = int(N1)
V1 = float(V1)
C2, N2, V2 = input().split()
C2 = int(C2)
N2 = int(N2)
V2 = float(V2)
prod = N1 * V1 + N2 * V2
print(f'VALOR A PAGAR: R$ {prod:.2f}')