# Descobrindo ano bissexto 
ano = float (input('qual é o ano para analizar'))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 : 

    print (f'o ano {ano} é bissexto')

else : 

    (f'o ano {ano} , nao é bissexto')