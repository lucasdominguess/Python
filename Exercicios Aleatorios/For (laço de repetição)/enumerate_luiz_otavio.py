lista = ['maria','helena','luiz']
lista_enumerada = enumerate(lista) 


for item in lista_enumerada : #vai exibir item por item da lista 
    print (item) #Saida : (0,'maria') (1,'helena') etc...

for indice , item in lista_enumerada: #Usando enumerate dessa forma so usara 1 vez 
    print (item,indice) #item é o valor (string) 
    #indice é a numeraçao de cada valor (int )

#agora ultilizando o for sem que o enumerate se esgote(aula 89 L.O(udemy))
for indice , item in enumerate(lista) : #enumerate chamando direto na lista
    print (item,indice)