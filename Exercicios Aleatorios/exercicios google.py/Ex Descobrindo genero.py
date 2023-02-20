s=(input('Vc e de qual sexo')).strip().upper()

while s == 'F' or 'M': 
    
    if s == 'SAIR':
        print ('Fim do programa')
        break
    if s == 'F':
       print ('vc e do sexo feminino')
       s=(input('Vc e de qual sexo')).strip().upper()
    elif s == 'M':
        print ( 'vc e do sexo masculino') 
        s=(input('Vc e de qual sexo')).strip().upper()
    else:
            s=(input('Digite apenas M ou F ')).strip().upper()