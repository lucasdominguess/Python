cadastro = []

continuar = 'sim'

while continuar == 'sim' : 
    nome = input ('digite seu nome ')
    idade= input ('digite sua idade ')
    pais = input ('digite seu pais ')
    lista = [nome]
    lista.append(idade)
    lista.append(pais)
    cadastro.append(lista)
    continuar = input ('Deseja cadastrar mais pessoas?')
#print (lista)
#print (cadastro) 
print ('Lista de Pessoas cadastradas: ')


for pessoa in cadastro : 
    print (f'Nome:', pessoa[0] , 'idade: ', pessoa[1],   ' Pais: ' ,pessoa[2])

print (f'foram cadastradas {len(cadastro)} pessoas ')

