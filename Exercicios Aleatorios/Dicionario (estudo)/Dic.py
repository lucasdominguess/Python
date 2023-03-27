#criar uma lista de cadastro de funcionarios ultilizando dicionarios

dic_cadastro = {}

#criando condiçao de validaçao do loop 
iniciar_cadastro = (input('Deseja cadastrar funcionarios? ')).strip().upper() 
   
while iniciar_cadastro == 'SIM' : 
    nome = (input('Digite o nome do funcionario ')).strip()
    idade =int (input('Digite a idade do funcionario '))
    salario = int (input('Digite o salario que o funcionario ira receber '))
    cidade = (input('qual cidade de nascimento'))
    #adcionando dados coletados para o dicionario
    dic_cadastro.setdefault(nome, []).append(idade) #set dafault usado em dicionario para adcionar dados 
    dic_cadastro.setdefault(nome, []).append(salario)
    dic_cadastro.setdefault(nome,[]).append(cidade)
    iniciar_cadastro = (input('Deseja cadastrar funcionarios? ')).strip().upper() 
print (dic_cadastro) # saida : {'lucas': 18 , 2000}

for funcionario , idade  in dic_cadastro.items() : 
    print (f'funcionario:',funcionario ,'tem ',idade[0] , 'anos' , 'e recebera R$',idade[1] ,'Nascido em' ,idade[2])
