numero = int (input('Digite um numero ')) 
resto = numero % 2 #usando resto da divisao por 2 , para saber se o numero é par ou impar 

if numero 
if  resto == 0: #se o resto da divisao for igual 0  é par
    print (f'o numero {numero} é par')
else: #se nao , sera impar e caira nesse else 
    print (f'numero {numero} é impar' ) 

#Baseando na qtd de letras no primeiro nome 
nome = (input ('Digite seu primeiro nome ')) 
qtdl = (len(nome)) #lendo e convertendo qtd de letras no nome

if qtdl <= 4 :   #se qtdl for menor ou igual 4 
    print ('seu nome é muito curto ') 
elif qtdl ==5 or qtdl <= 7 : #se qtdl for igual 5 ou menor igual 7 
    print('seu nume esta na media ')
elif qtdl >=8 : #se qtdl for maior ou igual 8 
    print ('seu nome é muito grande ')
