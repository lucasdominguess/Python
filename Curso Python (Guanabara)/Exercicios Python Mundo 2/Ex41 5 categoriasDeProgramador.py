from datetime import date
data = date.today().year 


nasc  = int (input('Digite o ano que vc nasceu '))
idade = data - nasc 

if idade >= 25 :
    print (f'Voce tem {idade} anos , e é um programador nivel SENIOR')

elif idade >=20 and idade <25 : 
    print(f'voce tem {idade} anos de idade , é um programador nivel PLENO')

elif idade >=15 and idade <20 : 
    print(f'voce tem {idade} anos de idade , é um programador nivel JUNIOR')

elif idade >=10 and idade <15 : 
    print(f'voce tem {idade} anos de idade , é um programador nivel TRAINNER ')
 
elif  idade >=5 and idade <10 : 
    print(f'voce tem {idade} anos de idade , é um programador nivel ESTAGIARIO')
elif idade <5 : 
    print ('vc ainda nao e um programador') 
#dica !! 
#comecar de cima pra baixo . do menor pro maior assim : 
#nao tem a necessidade de verificar as segunda etapa "dps do and" 
#pois o algoritimo ja passou pelas condiçoes menores e ira avaliar conforme a idade for aumentando

