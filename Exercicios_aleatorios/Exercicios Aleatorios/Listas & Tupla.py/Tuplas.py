#tuplas sao imutaveis 

lista_nomes = 'maria' , 'joao' , 'luiz ' #tupla e uma lista imutavel 
#nao e necessario usar parenteses 


lista_nomes = list(lista_nomes) #tarnformando para lista

print (type(lista_nomes)) #mostrando tipo do objeto (saida = lista)

lista_nomes = tuple(lista_nomes) #transformando novamente para tupla
print (type(lista_nomes)) #exibindo objeto com tipo auterado (saida = tupla)
