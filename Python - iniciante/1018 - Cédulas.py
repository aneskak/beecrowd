valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtd_cedulas = int(valor/nota)
    print(f'{qtd_cedulas} nota(s) de R$ {nota},00')
    valor -= qtd_cedulas * nota