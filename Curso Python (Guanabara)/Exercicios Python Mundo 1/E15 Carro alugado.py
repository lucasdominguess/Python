'''escreva um programa que pergunte a quantidade de Km rodados por um carro alugado

e a quantidade de dias pelos quais ele foi alugado . calcule o preço a pagar 

sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado.''' 


Preçodia = float (60)

Preçokm = float (0.15) 


dia =  float (input('por quantos dias o carro foi alugado??'))

km = float (input('digite quanto kms foram rodados')) 


Resuldia = dia*Preçodia 

Resulkm = km*Preçokm


print (f'valor rodado {km*Preçokm:.2f} , valor por dias alugados {Resuldia:.2f} \n valor total R${Resulkm+Resuldia:.2f}')