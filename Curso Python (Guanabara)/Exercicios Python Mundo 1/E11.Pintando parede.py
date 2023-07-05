lp = float (input('qual a largura da sua parede '))
ap = float (input ('qual a altura da sua parede ')) 

M2 = lp*ap 
lt =  2.0 #qtd de latas usadas para metros de parede (1 lata para cada 2 metros) 
lt2 = M2/lt 

print (f'Sua parede tem no total {M2} Metros quadrados')
print (f'vc precisara de {lt2:.2f} latas de tinta')