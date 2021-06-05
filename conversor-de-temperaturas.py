#           CONVERTER TEMPERATURA

c = float(input('Informe a temperatura ºC:')) # PERGUNTA A TEMPERATURA EM ºC
f = ((9 * c) / 5) + 32 # MULTIPLICA 9 x c / 5 + 32
print('{:.2f}ºC equivale à {:.2f}ºF'.format(c,f)) # MOSTRA A CONVERSÃO EM ºF
