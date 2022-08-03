a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)

map = (2*a + 3*b + 4*c + 1*d) / (2+3+4+1)
print(f'Media: {map:.1f}')

if map >= 7.0:
    print("Aluno aprovado.")
elif map <5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    ne = float(input())
    print(f'Nota do exame: {ne:.1f}')
    me = (ne + map) / 2
    if me >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {me:.1f}')
