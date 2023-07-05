from time import sleep
n1 = float (input('Digite primeira nota'))
n2 = float (input('Digite segunda nota '))


media = (n1+n2)/2 #  calculando a media das notas com /2 

print ('aguarde , calculando media ... gerando nota final do aluno...')
sleep(3)
print (f' a media final do aluno foi {media} ')
sleep (2)
if media >= 7 : 
    print ('Aluno aprovado !') 
elif media >=6 and media <7 : 
    print ('aluno em recuperação')

elif media <6 : 
    print ('Aluno reprovado')


          