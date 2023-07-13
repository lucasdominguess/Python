'''validando nota de 0 a 10 '''


nota = int (input('Digite uma nota entre 0 e 10 '))

while nota > 10 :
    print (f'vc digitou a nota {nota}')
    nota = int (input('digite somente entre 0 a 10 '))


if nota <=10: 
     print (f'vc digitou a nota {nota}')


print ('Acabou') 


def peso(peso):

    if peso >= 50:
        print("peso esta correto")
    else:
        peso = input('digite seu peso novamente')
    
    