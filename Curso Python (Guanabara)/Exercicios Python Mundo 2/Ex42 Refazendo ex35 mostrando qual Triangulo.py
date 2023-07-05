r1 = float (input('digite um numero'))
r2 = float (input('digite outro numero'))
r3 = float (input('digite um terceiro numero'))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2 : #o seguimentos tem que ser menor que a a soma dos outros dois
    print ('Sim essa combiaçao de tamanhos podem formar um triangulo')
    if r1 == r2 == r3 : 
        print('Triagulo EQUILATERO')
    if r1 != r2 != r3 != r1 :
        print ('Triangulo ESCALENO')
    else : 
        print ('triangulo ISÓSCELES')
else : 
    print ('Opss .. essa conbinaçao nao podem formar um triangulo ')