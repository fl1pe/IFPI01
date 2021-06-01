#           PINTANDO A PAREDE

larg = float(input( 'Largura da parede: '))
alt = float(input('Altura da perede: '))
area = larg * alt
tinta = area / 2
print('Dimesão de {}x{} e àrea de {}m²'.format(larg,alt,area))
print('{:.2f}L de tinta necessàrio para pintar a parede!'.format(tinta))