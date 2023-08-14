
# valorInicial = int(input('Digite o valor Ofertado pela Empresa '))
# part_adv = valorInicial * 30/100 
# valorfinal= valorInicial-part_adv


# print (part_adv)
# print (valorInicial-part_adv)

# print (f'O valor do acordo R$ {valorInicial:.2f} \n valor da parte do advogado R${part_adv:.2f} \n  sobrara R${valorfinal:.2f}')

def valorAcordo(valorInicial):
    mostralinha = 10*'---'
    part_adv = valorInicial * 30/100 
    valorfinal = valorInicial-part_adv
    
    return print (f'{mostralinha} \n O valor do acordo R$ {valorInicial:.2f} \n valor da parte do advogado R${part_adv:.2f} \n sobrara R${valorfinal:.2f} \n {mostralinha}')


valorAcordo(30000) 
 

