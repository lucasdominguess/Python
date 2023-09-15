from random import randint 
from time import sleep 

computador = randint (0,5) #faz o computador randomizar



player = float (input('Digite um numero'))

print ('Pensando ...')

sleep(3) #pc espera '3' segundos ate executar porxima ação


print (f'vc digitou {player}e o computador digitou {computador}')

