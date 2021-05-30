print('SAIBA SEU DESCONTO!\t')

print("QUANTOS PRODUTOS VOÇÊ QUER ADCIONAR?\t\n1-PRODUTO\n2-PRODUTOS\n3-PRODUTOS")
a = int(input('\tDigite a quantidade de produtos: '))
if a == 2:
    p1 = float(input('Valor do 1ºproduto? '))
    p2 = float(input('Valor do 2ºproduto? '))
    total = p1 + p2
    print('VALOR TOTAL: {:.2f}'.format(total))
    p4 = int(input('Informe seu desconto: '))
    a1 = (print('Desconto de {}% aplicado!'.format(p4)))
    b1 = p4 / 100
    desc_ganh = total * b1
    print('VALOR INICIAL:\nR${:.2f}'.format(total))
    print('DESCONTO GANHO:\nR${:.2f}'.format(total * b1))
    print('VALOR FINAL:\nR${:.2f}'.format(total * (1 - b1)))
elif a == 3:
    p1 = float(input('Valor do 1ºproduto? '))
    p2 = float(input('Valor do 2ºproduto? '))
    p3 = float(input('Valor do 3º produto? '))
    total = (p1 + p2 + p3)  # soma os três produtos
    print('VALOR TOTAL: {:.2f}'.format(total))
    p4 = int(input('Informe seu desconto: '))  # pergunta de quanto é o desconto
    a1 = (print('Desconto de {}% aplicado!'.format(p4)))  # mostra o a mensagem de quanto foi aplicado (desconto)
    b1 = p4 / 100  # divide o total por 100
    desc_ganh = total * b1
    print('VALOR INICIAL:\nR${:.2f}'.format(total))  # mostra o valor inicial da soma dos três produtos
    print('DESCONTO GANHO:\nR${:.2f}'.format(total * b1))  # mostra o desconto ganho
    print('VALOR FINAL:\nR${:.2f}'.format(total * (1 - b1)))
elif a == 1:
    p1 = float(input('Digite o valor do produto: '))
    total = p1
    a1 = int(input('De quanto é seu desconto? '))
    b1 = a1 / 100
    desc_ganh = total * b1
    print('VALOR INICIAL:\tR${:.2f}'.format(total))
    print('DESCONTO GANHO:\tR${:.2f}'.format(total * b1))
    print('VALOR FINAL:\tR${:.2f}'.format(total * (1 - b1)))
elif a > 3:
    print('\n\tOPÇÃO INVÁLIDA!')
