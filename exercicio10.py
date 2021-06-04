produto = float(input('Valor do produto R$')) # LER O PREÇO DO PRODUTO
print('Pagamento ÀVISTA ou PARCELADO?\n \ntecle (1) para àvista (2) para parcela.') # PERGUNTA A FORMA DE PAGAMENTO
n1 = int(input()) # INFORMA A FORMA DESEJADA
if n1 ==1: # SE FOR AVISTA GANHA 10% DE DESCONTO
    print('10% de DESCONTO!!!!') # MOSTRA O DESCONTO
    p1 = produto - (produto * 10 / 100) # CALCULA O PREÇO ORIGINAL - O DESCONTO
    print('Valor com desconto {:.2f}R$'.format(p1)) # MOSTRA O VALOR FINAL COM DESCONTO
elif n1 ==2: # SE FOR PARCELADOR TEM UM AUMENTO DE 8%
    print('8% de aumento sobre o valor produto.') # INFORMA SOBRE O AUMENTO
    p1 = produto + (produto * 8 / 100) # CALCULA O VALOR MAIS O AUMENTO
    print('Valor final {:.2f}R$'.format(p1)) # MOSTRA O VALOR FINAL COM O AUMENTO
    print('2x de {:.2f}R$'.format(p1 / 2)) # MOSTRA O VALOR DAS PARCELAS
