'''faça um programa que leia algo pelo teclado e mostre o seu tipo promitivo e todas as informaçoes sobre ele'''

a = input('Digite algo') 
print ('o tipo primitivop desse valor e ',type(a)) 
print ('so tem espaços',a.isspace())
print ('é numerico',a.isnumeric())
print ('é alfabetico',a.isalpha())
print ('é alfanumerico',a.isalnum())
print ( 'é maiusculas',a.isupper())
print ('esta em minusculas', a.islower())
print ('esta capitalizada?',a.istitle())
