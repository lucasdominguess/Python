
peso = float (input('Digite seu peso'))
altura = float (input ('Digite sua altura'))
imc = peso / (altura * altura ) 
#imc = float(input('Digite seu Imc')) Desativado 

print (f'Seu indice de massa corporal é {imc:.2f}')
if imc <= 18.5 : 
    print ('Abaixo do peso')
elif imc <= 25: 
    print('peso ideal')
elif imc <= 30 : 
    print ('sobrepeso')
elif imc <=40: 
    print('Obesidade')
else :
    print ('Obesidade morbida')


#linha1 = f'{nome} tem {altura :.2f} de altura,' #é possivel usar f-string tambem em variaveis 
#linha2 = f'{peso}Kg'   #EX : Uso de f-string dentro de uma nova variavel recebendo valores de outras variaveis '

#abaixo de 18.5 : Abaixo do peso 
#entre 18.5 a 25 : Peso ideal 
#de 25 ate 30: Sobrepeso 
#De 30 ate 40 : Obesidade 
#Acima de 40: Obesidade Morbida 