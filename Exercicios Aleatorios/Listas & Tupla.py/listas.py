'''cuidado com dados mutaveis ''' #Exemplo: 
lista_a = ['luiz', 'maria']
lista_b = lista_a # lista_b recebendo o valor da lista_a (apontando para o msm valor na memoria)
lista_a[0] ='qualquer coisa' #ao alterar o valor da lista_a tbm altera a da lista_b
'''Para fazer uma copia de lista ultilize lista.copy()'''
lista_b = lista_a.copy() 


#.......+01234
#.......-54321
string ='ABCDE' 
lista = ['lucas','jenifer','heitor','maria','ana'] #Criar lista ultilzando list() Lista suporta qlq tipo valor (bool , str , int ,float , true , false )
 
#interagindo com a string/itens da lista
print (lista[1]) #exibindo item da lista
print (lista[0:3]) #exibindo 0 a 2 na lista #sempre ocultara o ultimo numero digitado Ex de e0 a 4 .. exibira de 0 a 3 
print (lista[0].upper(), type(lista[0])) #type para saber o tipo do valor 0 da lista
lista.append('euro') #adcionando +1 valor a lista , tbm adc valor selecionado basta passar no indice ex: lista.append(5) 
lista.pop() #remove o ultimo item da lista , tbm remove valor selecionado basta passar no indice ex: lista.pop(5)  
print (lista[-1]) #exibindo o valor adcionado (-1 ultimo valor)
del lista[2] #deletando valor 2 da lista
print (lista) #exibi lista alterada sem o valor 2 
lista.remove('dois')# remove o caractere digitado entre aspas o conteudo
lista.clear() #usado para limpar lista completa
lista.insert(3,5) #inserir na posiçao '3' o numero '5' (lista.index('maria'))#index usado para saber a posicao do caracteres , (iniciando do zero)
lista.count('maria') #count usado para mostrar a qtd de palavra ou valor expecificos numa frase/lista
lista.sort() #ordena todos os valores da lista  
lista.sort(reverse=True)#Ordena de forma contraria os valores da lista
