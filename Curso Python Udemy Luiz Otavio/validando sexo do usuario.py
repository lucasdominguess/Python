nome = (input("digitre seu nome "))
idade = float (input('digite sua idade '))

sexo = (input('digite seu sexo ')).upper().strip()


while sexo != 'FEMININO'or 'MASCULINO':

     print ('digite apenas masculino ou feminino') 

     break

if sexo == 'FEMININO': 

    print ('vc e do sexo feminino')

elif sexo == 'MASCULINO': 

    print ('vc e do sexo masculino')


