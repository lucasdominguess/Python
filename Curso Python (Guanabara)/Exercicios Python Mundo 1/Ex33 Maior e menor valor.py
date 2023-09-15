

lista = []


for i in range(5) : 

    valores = float (input('digite 5 valores aleatorios'))

    lista.append(valores)
  

print (f'os numeros digitados foram {lista}')

print (f'o maior numero é {max(lista)}')

print (f'o menor numero é {min(lista)}') 
print (f'foram digitados {len(lista)}')

print (f'a soma de todos os numeros digitados são {sum(lista)}')

print (f'o terceiro valor digitado foi {lista[2]}')