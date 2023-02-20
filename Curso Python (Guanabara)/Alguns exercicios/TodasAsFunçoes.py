lista = ['1','9','4','2','6','7','8']

'''adcionando itens da lista'''

#lista.append('seis') #adciona um elemento no final da lista
#lista.insert(2,'sete') #adciona elemento na posiçao '2' da lista , assim dando outra ordem

 '''removendo itens da lista'''

'''del lanche [3] ''' # remove algo especifico da lista 
'''lanche.pop(3)'''   #remove o ultimo caractere da lista , mas pode usar ('valor') tbm 
'''lanche.remove('dois')''' # remove o caractere digitado entre aspas o conteudo

'''lista.sort()''' #ordena todos os valores da lista  
'''lista.sort(reverse=True)''' #Ordena de forma contraria os valores da lista

'''Usando for em lista ''' 

prato =  ['arroz', 'feijao' ,'carne' , 'salada' ] #lista criada 

for alimento in prato:   #para cada alimento no prato , faça isso 
    print (f'{alimento} alimentos saudavel ',end='') #end='' faz a frase seguir na mesma linha

for um , alimento in enumerate(prato):# para cada 'um' alimento detro de prato de a  posiçao(numeraçao)
    print(f'na posiçao {um} o alimento é {alimento}!') 

'''print (len(c)) ''' #funçao len , ler a qtd de caracteres na frase selecionada 
'''print (c.count(3)) '''#count usado para mostrar a qtd de caracteres expecificos numa frase 
'''#print (c.index(5))''' #index usado para saber a posicao do caracteres , (iniciando do zero)