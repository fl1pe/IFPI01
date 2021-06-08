print('____________________ESCOLHA UMA FUNÇÃO____________________')
print('\033[0;30;42m1-Média de notas.\n2-Cálculo de IMC.\n3-Conversor de temperatura.\n4-Dobro, Triplo e Raiz quadrada.\n5-Conversor de medidas.\n6-Tabuada.\n7-Conversor de moedas.\n8-Tinta necessária pra pintar uma parede')
var1= int(input('\n\tInforme a opção desejada! '))
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
elif var1 == 6:
    num = input('Informe um número: ')
    num1 = int(num)
    if is_integer(num) == False:
        print('Número inválido!\ninforme um número inteiro')
