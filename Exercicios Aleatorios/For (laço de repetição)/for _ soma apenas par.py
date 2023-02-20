#Desafio 50 guanabara 
'''Programa para ler 6 numeros digitados pelo usuario
e ira ler apenas numeros pares'''


n1 = 0
for n in range (0,5):
    numero = int (input('Digite um numero'))
    if numero % 2 == 0: #Verificando se o resto da divisao é 0 
         n1+=numero #se for ai soma com os demais
    
print (n1)
