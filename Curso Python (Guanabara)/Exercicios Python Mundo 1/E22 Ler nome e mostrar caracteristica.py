'''crie um programa que leia o nome de uma pessoa e mostre  '''
'''Nome com todas as letras maiusculas '''
'''Nome com todas as letras minusculas ''' 
'''quantas letras tem ao todo (sem contar espaços)'''
'''quantas letras tem o primeiro nome'''

nome = (input('Digite seu nome completo')).strip() #serve para  ignorar os espaços antes e depois

print ('Analisando seu nome ...')
print(nome.upper()) #Deixando Maiusculas
print(nome.lower()) #Deixando Minusculas
print(len(nome)- nome.count(' ')) #len mostra qtd letras, nome.cout ('  ') contador de espaço entre as letras 
#  len(nome) - nome.cout(' ') subtrai a letras dos espaços encontrados

print (f'seu primeiro nome tem ', {nome.find(' ')} ) #identifica e enconta o primeiro espaço na frase 
separa = nome.split() #cria uma lista com o nome completo separando cada um para uma eventual consulta
print (f'seu primeiro nome é {separa[0]} , ele tem {len(separa[0])}letras') #seleciona palavra na posiçao 0
print (f'o seu segundo nome é {separa[1]} , e tem {len(separa[1])} letras') 