print('\t\t\n>>>>>>>>>>>>>INFORME SUAS NOTA<<<<<<<<<<<<<<<<')
total = 0
s= 0
while total<3:
    n1 = float(input('\tNota: '))
    s += n1
    total +=1
m = s / 3
if m >6 and m <10:
    print('\n\tMédia de {:.1f}\tAPROVADO!'.format(m))
elif m <6:
    print('\n\tMédia de {:.1f}\tRECUPERÇÃO!'.format(m))
