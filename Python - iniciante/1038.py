cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)
 
total = "Total: R$ "

if cod == 1:
    print(f'Total: R$ {4.00*qtd:.2f}')
elif cod == 2:
    print(f'Total: R$ {4.50*qtd:.2f}')
elif cod == 3:
    print(f'Total: R$ {5.00*qtd:.2f}')
elif cod == 4:
    print(f'Total: R$ {2.00*qtd:.2f}')
elif cod == 5:
    print(f'Total: R$ {1.50*qtd:.2f}')

