print('____________________ESCOLHA UMA FUNÇÃO____________________')
print('1-Média de notas.\n2-Cálculo de IMC.\n3-Conversor de temperatura.\n4-Dobro, Triplo e Raiz quadrada.\n5-Conversor de medidas.\n6-Tabuada.\n7-Conversor de moedas.\n8-Tinta necessária pra pintar uma parede')
var1= int(input('\n\tDigite a opção desejada! '))
if var1 == 1:
    n1 = float(input('Digite sua 1º nota '))
    n2 = float(input('Digite sua 2º nota '))
    n3 = float(input('Digite sua 3º nota '))
    m = (n1 + n2 + n3) / 3
    print('Média de {:.2f} pontos!'.format(m))
elif var1 ==2:
