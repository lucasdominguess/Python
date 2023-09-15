cont = ('zero','um','dois ','tres','quatro','cinco','seis','sete','oito','nove','dez')


while True:

    num = float (input('Digite um numero entre 0 e 10 '))

    if 0 <= num <= 10 : #se menor ou igual zero , menor ou igual 10 

        break   

    else: #se nao 

     print ('tente novamente')


print (f'voce digitou o numero {cont[num]}') 


