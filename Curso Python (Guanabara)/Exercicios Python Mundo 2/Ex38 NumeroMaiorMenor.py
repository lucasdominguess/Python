from time import sleep

num1 = int (input('Digite um numero'))
num2 = int (input('Digite outro numero '))

print ('verificando qual numero é maior.. Aguarde um instante ')

sleep(3) #tempo de espera '3 seg' ate saida do resultado

if num1 > num2 : 
    print (f'O primeiro numero é o maior ')
elif num2> num1 : 
    print (f'o segundo numero é o maior')
elif num1 == num2 : 
    print ('os numeros sao iguais..')

