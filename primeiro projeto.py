import math
print('____________________ESCOLHA UMA FUNÇÃO____________________')
print('''\033[1;33;40m
>>>>>>\t1-Média de notas.
>>>>>>\t2-Cálculo de IMC.
>>>>>>\t3-Temperatura corporal.
>>>>>>\t4-Dobro, Triplo e Raiz quadrada.
>>>>>>\t5-Conversor de medidas.
>>>>>>\t6-Tabuada.
>>>>>>\t7-Seno, cosseno e tangente de uma ângulo.
>>>>>>\t8-Tinta necessária pra pintar uma parede''')
var1= int(input('''---------------------------------------------
\033[1;32;40m\t\tInforme a opção desejada! '''))
if var1 == 1:
    n1 = float(input('Digite sua 1º nota '))
    n2 = float(input('Digite sua 2º nota '))
    n3 = float(input('Digite sua 3º nota '))
    m = (n1 + n2 + n3) / 3
    print('Média de {:.2f} pontos!'.format(m))
elif var1 == 2:
    alt = float(input('Informe sua altura: '))
    peso = float(input('Informe seu peso: '))
    imc = peso / (alt * alt)
    if imc < 18.5:
        print('CLASSIFICAÇÃO: {:.2f}'.format(imc))
        print('Subnutrido!')
    elif imc >= 18.6 and imc < 24.9:
        print('CLASSIFICAÇÃO: {:.2f}'.format(imc))
        print('Peso normal!')
    elif imc >= 25 and imc <=29.9:
        print('CLASIFICAÇÃO: {:.2f}'.format(imc))
        print('Sobreso!')
    elif imc >= 30 and imc <= 34.9:
        print('CLASSIFICAÇÃO: {:.2f}'.format(imc))
        print('Obesidade grau I!')
    elif imc >= 35 and imc <= 39.9:
        print('CLASSIFICAÇÃO: {:.2f}'.format(imc))
        print('Obesidade grau II!')
    elif imc > 40:
        print('CLASSIFICAÇÃO: {:.2f}'.format(imc))
        print('Obesidade grau III!')
elif var1 == 5:
    m = float(input('Informe os metros: '))
    print('{}M equivale à \n{}CM\n{}MM\n{}KM'.format(m,m*100,m*1000,m/1000))
elif var1 == 8:
    alt = float(input('''Informe à altura da parede: '''))
    larg = float(input('''Informe à largura da pared: '''))
    area = alt * larg
    tinta = area / 2
    print(f'''
Dimensão da paredede {math.ceil(alt)}x{math.ceil(larg)}
Com uma àrea de {area}m²
Serão necessário {math.ceil(tinta)}L de tinta para pintar à parede.''')
elif var1 == 7:
    an = float(input('Informe o ângulo:'))
    sen = math.sin(math.radians(an))
    coss = math.cos(math.radians(an))
    tan = math.tan(math.radians(an))
    print(f'''
O ângulo de {an}º tem o 
Seno de {sen:.2f}
Cosseno de {coss:.2f}
Tangente de {tan:.2f}''')
elif var1 == 6:
    print('>' * 15, 'TABUADA','<' * 15)
    n = int(input('''
\033[7;mInforme um número: '''))
    print('-' * 12)
    print('{} x {:2} = {}'.format(n, 1, n * 1))
    print('{} x {:2} = {}'.format(n, 2, n * 2))
    print('{} x {:2} = {}'.format(n, 3, n * 3))
    print('{} x {:2} = {}'.format(n, 4, n * 4))
    print('{} x {:2} = {}'.format(n, 5, n * 5))
    print('{} x {:2} = {}'.format(n, 6, n * 6))
    print('{} x {:2} = {}'.format(n, 7, n * 7))
    print('{} x {:2} = {}'.format(n, 8, n * 8))
    print('{} x {:2} = {}'.format(n, 9, n * 9))
    print('{} x {:2} = {}'.format(n, 10,n * 10))
    print('-' * 12)
elif var1 == 3:
    t = float(input('INFORME SUA TEMPERATURA EM ºC: '))
    b1 = t
    if b1 <= 36.5:
        print('\tHipotermia!')
    elif b1 >= 36.5 and b1 < 37: \
            print('\tNormal!')
    elif b1 >= 37 and b1 < 38:
        print('\tEstado febril!')
    elif b1 >= 38:
        print('\tFebre!')
