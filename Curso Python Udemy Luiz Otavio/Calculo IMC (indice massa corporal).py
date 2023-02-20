nome = (input('Digite seu nome '))
peso = float (input('Digite seu peso'))
altura = float (input ('Digite sua altura'))
imc = peso / (altura * altura ) 


print (f'Ola {nome}') 
print (f'Seu indice de massa corporal é {imc:.2f}')



linha1 = f'{nome} tem {altura :.2f} de altura,' #é possivel usar f-string tambem em variaveis 
linha2 = f'{peso}Kg'   #EX : Uso de f-string dentro de uma nova variavel recebendo valores de outras variaveis 

