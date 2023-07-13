'''Escreva um programa que recebe uma lista de números inteiros do usuário,
 e imprime na tela a soma dos números pares da lista. '''

lista = []
entrada = 0 
lista_impar = []
while entrada <6 :
        num = int (input("Digite numeros inteiros para a soma"))
        if num %2 == 0 : 
            lista.append (num) 
            entrada+=1 
     
        else :
            lista_impar.append  (num)
            entrada+=1 
print (f'a soma dos numeros pares foi ',sum(lista))

if len(lista) > 0 :
      print (f'foram digitados tbm {len(lista)} numeros pares')            
if len(lista_impar) > 0 :
     print (f'foi digitados {len(lista_impar)} numeros impares')
    

