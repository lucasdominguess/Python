''' Programa que leia velocidade de um carro e diga se foi multado 
adcionando 7 reais para cada km excedido'''


velocidade = int (input('Digite a velocidade do carro'))
multa =  velocidade - 80 
valor = float (multa)*7
if velocidade > 80 : 
    print ('Voce excedeu os 80Km/h e foi multado ')
    print (f'multa aplicada no valor de R${valor:.2f} ')
else : 
    print ('Velocidade permitida')