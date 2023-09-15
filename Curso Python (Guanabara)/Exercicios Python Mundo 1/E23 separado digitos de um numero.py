num = float (input('Digite numero'))

unidade = num // 1 % 10  

dezena  = num // 10 % 10 

centena = num // 100 % 10   

milhar = num // 1000 % 10  


print (f'analisando o numero {num} ... ')

print (f'unidade: {unidade}') 

print (f'dezena : {dezena}') 

print (f'centena : {centena}') 

print (f'milhar : {milhar}')


#ler numero e mostra cada numero separado , como unidade , dezena , centena e milhar 