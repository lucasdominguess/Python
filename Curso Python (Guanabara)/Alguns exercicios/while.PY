s=(input('Vc e de qual sexo')).strip()

while s != 'F': #Preciso resolver como reconhecer S como F e tbm M  
    s=(input('Digite apenas M ou F ')).strip()
    

if s == 'F':
    print ('vc e do sexo feminino')
elif s == 'M':
    print ( 'vc e do sexo masculino') 

else:
    print ('Digite novamente')


