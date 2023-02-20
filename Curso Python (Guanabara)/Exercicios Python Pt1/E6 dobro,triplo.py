'''exercicio 06 Dobro , triplo , raiz quadrada''' 

n = int (input('Digite um numero')) 
d = n*2 #o valor de N vezes 2 
t = n*3 
rq = n**(1/2) #Usar sinal ** , usar parenteses para forçar o calculo primeiro 

print (f'o dobro de {n} é {d} o triplo é {t} e a raiz quadrada é {rq:.2f}') #usar :.2f Para quebrar casas decimais na raiz quadrada 
