#testandopo 
'''for c in range(0,5):
    print ('lucas 5 vezes')'''

'''Usando for em lista ''' 

prato =  ['arroz', 'feijao' ,'carne' , 'salada' ] #lista criada 

#for alimento in prato:   #para cada alimento no prato , faça isso 
 #   print (f'{alimento} alimentos saudavel ',end='') #end='' faz a frase seguir na mesma linha

for um , alimento in enumerate(prato):  #
    print(f'na posiçao {um} o aliemnto é {alimento}!') 