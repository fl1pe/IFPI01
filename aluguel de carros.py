#           ALUGUEL DE CARROS
da = int(input('Por quantos dias o veiculo foi alugado? '))
km = int(input('Km rodados? '))
total = (da * 60) + (km * 0.15) # CUSTO DO ALGUEL POR DIA R$60, e R$0.15 POR KM RODADOS
print('Total a pagar {:.2f}R$'.format(total))
