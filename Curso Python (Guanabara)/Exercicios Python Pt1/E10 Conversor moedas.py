''' faça um programa leia e que converta uma qtd de real e converta para dolar ''' 

real = float (input('quanto em dinheiro vc tem '))
dolar = real/5.18 # basta dividir a var real pelo valor do dolar 

print (f'Voce possui R${real:.2f} reais e pode comprar ${dolar:.2f} dolares')