nome = []
contador = 0
while contador < 4:
    nome.append (input('Digite seu nome')) 

    contador+=1
print (f'os nomes digitados foram {nome}')
print (f'o primeiro nome digitado foi {nome[0]}')
print (f'o ultimo nome digitado foi {nome[-1]}')