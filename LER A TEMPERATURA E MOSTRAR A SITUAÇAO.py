##   QUESTAO 6.0 ###


while (True):
    a1 = float(input('INFORME SUA TEMPERATURA EM ºC: '))
    b1 = a1
    if b1 <= 36.5:
        print('\tHipotermia!')
    elif b1 >= 36.5 and b1 < 37:\
        print('\tNormal!')
    elif b1 >= 37 and b1 < 38:
        print('\tEstado febril!')
    elif b1 >= 38:
        print('\tFebre!')