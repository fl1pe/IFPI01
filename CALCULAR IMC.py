#           CALCULAR IMC        #
# QUUESTAO 8.1.2

alt = float(input('Informe sua altura: \t'))
peso = float(input('Informe seu peso:\t '))
n1 = alt * alt
n2 = n1
imc = f'{peso / n2:.2f}'
if float(imc) < 20:
    print('Subnutrido')
elif float(imc) >= 20 and float(imc) <= 24.9:
    print('\nCLASSIFICAÇÃO: ',imc)
    print('\n\tNormal')
elif float(imc) >= 25 and float(imc) <= 29.9:
    print('\nCLASSIFICAÇÃO :',imc)
    print('\n\tSobrepeso')
elif float(imc) >= 25 and float(imc) <= 29.9:
    print('\nCLASSIFICAÇÃO: ',imc)
    print('\n\tObesidade grau I')
elif float(imc) >= 30 and float(imc) <= 39.9:
    print('\nCLASSIFICAÇÃO: ',imc)
    print('\n\tPré-obeso')
elif float(imc) > 40:
    print('\nCLASSIFICAÇÃO: ',imc)
    print('\n\tObesidade')