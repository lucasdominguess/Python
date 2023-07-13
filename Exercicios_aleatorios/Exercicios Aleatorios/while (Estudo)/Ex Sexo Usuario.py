
n = 0 #variavel inicia a contagem do while #tbm da sequancia na continualao do while    

#Exercicio , descobrindo sexo do usuario
while n <=3: #condiçao  
    sexo = (input('Digite seu sexo')).upper().strip()
    if sexo == 'F':
        print ('voce e do sexo feminino')
    elif sexo == 'M': 
        print ('voce e do sexo masculino')
    else : 
        print ('Digite apenas F (feminino) e M (masculino)')
    n += 1 #importante dar seq na variavel adcionando valor 
print ('acabou')