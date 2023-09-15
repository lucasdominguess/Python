#soma de pares 

soma = 0

cont = 0

excluidos = 0

digitadosList = []

excluidosList = []

for i in range (1,7,): 
    num = float (input('Digite um numero')) 

    if num %2==0 : 

        soma = soma+num #soma de numeros validos

        cont = cont+1 #contagem qtos numeros validos

        digitadosList.append(num) #Adiciona numeros validos a lista

    else: 

        excluidos = excluidos+1 #contagem numeros excluidos

        excluidosList.append(num) #adciona numeros excluidos a lista


print (f'a soma dos numeros é {soma}')

print (f'quantos numeros validos foram digitados {cont}')


print(f' numeros excluidos {excluidos}')


print (f'lista de Numeros VALIDOS {digitadosList}')

print (f'lista de Numeros EXCLUIDOS {excluidosList}')


