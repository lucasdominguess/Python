from datetime import date  #usar date para saber o ano atual

atual = date.today().year #retona ano atual 



anoNascimento = float (input('Digite o ano do seu nascimento'))

idade = atual-anoNascimento


print (f' quem nasceu em {anoNascimento} tem {idade} anos de idade ')

if idade >18 : 

    saldo = anoNascimento+18 #retorna ano para o alistamento

    print (f'vc ja deveria ter se alistado ha {idade-18} anos atras \n seu alistamento foi em {saldo}')


elif idade <18 : 

    saldo = 18-idade #returna difereça entre 18 anos e a idade 

    print (f'ainda falta {saldo} anos para seu alistamento')

    print (f'seu alistamento sera em {atual+saldo}') #ano atual + a diferença para ober 18 anos 
    

elif idade == 18 : 

    print ('voce deve se alistar esse ano ')