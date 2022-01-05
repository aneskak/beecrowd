import math
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

try:
    delta = b ** 2 - 4 * a * c
    r1 = (- b + math.sqrt(delta)) / (2 * a)
    r2 = (- b - math.sqrt(delta)) / (2 * a)

    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))

except:
    print('Impossivel calcular')