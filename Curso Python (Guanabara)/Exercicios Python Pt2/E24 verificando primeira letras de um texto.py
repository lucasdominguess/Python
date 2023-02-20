'''Faca um programa que leia um nome de cidade e diga se ela comeca com o nome santo ''' 

cidade = str (input('Digite o nome da cidade'))
print (cidade[0:5].strip().upper() == 'SANTO') #em cidade , posiçao 0 ate 5 é igual str 'santo' 
#Retorna o valor verdadeiro o falso 

if cidade[0:5] == ('santo') : #para palavras grandes , use ex [0:5] 
    print ('ok , verificado!!!') 
else: 
    print ('Opa cidade nao reconhecida')