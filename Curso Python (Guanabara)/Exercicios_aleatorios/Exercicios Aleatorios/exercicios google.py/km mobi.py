km_franquia = 2520

km_rodados = int (input('qtos kms vc rodou esse mes ? '))
km_excedente = km_rodados-km_franquia

if km_franquia<km_rodados : 
    print (f'vc rodou total de {km_rodados}km')
    print (f'ultrapassou {km_excedente} km da franquia')
    print (f'convertendo .. vc recebera R${km_excedente*0.30}Reais')
else : 
    print (f'Voce rodou apenas {km_rodados}km. e nao atingiu a franquia de {km_franquia}km')
    #ok

