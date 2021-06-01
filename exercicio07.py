#           CONVERSOR DE MOEDAS /// COTAÇAO DIA 31/05/2021

while(True): # LAÇO DE REPETIÇÃO
    real = float(input('Digite o valor: R$'))
    print('Deseja converter em: \n1-DOLAR\n2-EURO\n3-BITCOIN')
    es = int(input('Escolha uma categoria: '))
    if es==1:
        print('{}R$ equivale à {:.2f}'.format(real,(real/5.21)))
    elif es ==2:
        print('{}R$ equivale à {:2f}'.format(real,(real/6.38)))
    elif es ==3:
        print('{}R$ equivale à {:.7f}'.format(real,real/192829.67))