''' crie uma tupla com os 20 primeiros colocados do brasileirao 
na ordem de colocaçao depois mostre 
a) apenas os 5 primeiros 
b os ultimos 4 
c) lsita com times em ordem alfabetica 
d ) aonde esta o tipe chapecoense ''' 

brasileiro = ('corinthias','palmeiras' , 'flamengo' ,'sao paulo ','vasco ', 'fluminence' , 
'ceara' , 'santos ','botafogo' , 'atletico mineiro' , 'athletico paranaense' ,'bahia' ,
 'cruzeiro' , 'chapecoense' , 'goias' , 'coritiba' , 'sport')

#print (len(brasileiro)) #qtos times tem [ok]
#print(f'Tabela do brasileirao{brasileiro}') #Mostra lista completa
#for t in brasileiro: 
    #print (t)   #Mostra lista completa em ordem cima pra baixo 

#print (f'os ultimos colocados sao {brasileiro[-4:]}') #ultimos colocados
#print (f'os primeiros colocados sao {brasileiro[0:5]}') #primeiros colocados 

#print (f'Times em ordem alfabetica {sorted (brasileiro)}') #ordem alfabetica 
print (f'o coritiba esta na posicao {brasileiro.index("coritiba")+1}') #para saber a posicao do time , 
#+1 mostra a posiçao correta 