a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

valido = b > c 
valido = valido and d > a
valido = valido and c + d > a + b
valido = valido and c > 0 and d > 0
valido = valido and a % 2 == 0
if valido:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')