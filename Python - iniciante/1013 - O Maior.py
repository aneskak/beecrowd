a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorab = (a+b+abs(a-b))/2

if c < maiorab:
    print(int(maiorab), 'eh o maior')
elif c > maiorab:
    print(c, 'eh o maior')