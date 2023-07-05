from datetime import date  #usar date para saber o ano atual
atual = date.today().year


anoNascimento = int (input('Digite o ano do seu nascimento'))
idade = atual-anoNascimento


print (f' quem nasceu em {anoNascimento} tem {idade} anos de idade ')
if idade >18 : 
    print (f'vc ja deveria ter se alistado ha {idade-atual} anos atras \n seu alistamento foi em {atual-idade}')

elif idade <18 : 
    print (f'ainda falta {tempoAlistamentoRestante} anos para seu alistamento')

elif idade == 18 : 
    print ('voce deve se alistar esse ano ')