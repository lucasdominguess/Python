
#Realizando contas (adição)
conta = (input('Vamos realizar contas? S/N?')).upper().strip()

while conta == 'SIM': 
    n1 = int (input('digite um numero'))
    n2 = int (input ('digite outro numero')) 
    print (f'a soma do numero {n1} e {n2} é {n1+n2}') 
    conta = (input('Vamos realizar novas contas? S/N?')).upper().strip()
else : 
    print ('Ok quem sabe mais tarde :)')