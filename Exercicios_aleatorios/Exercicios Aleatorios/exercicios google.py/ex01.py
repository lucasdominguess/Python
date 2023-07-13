'''Escreva um programa que receba uma string do usuário e conte quantas vezes cada letra 
aparece na string.
 Em seguida, imprima os resultados para o usuário. Use um loop for para iterar sobre a string 
e um dicionário para armazenar o número de ocorrências de cada letra.'''

frase = input('Digite uma frase ')
qtd_letras = len(frase)

for qtd_letras in range(frase): 
    print (qtd_letras,frase )
    
