palavra_secreta = 'perfume'
letras_acertadas = ' '
numero_tentativas = 0
while True : 
    letra_digitada = input('digite uma letra')
    numero_tentativas += 1

    if len (letra_digitada) >1 : 
      print ('Digite apenas uma letra.')
      continue 
    palavra_formada = ''
    if letra_digitada in palavra_secreta: 
        letras_acertadas+= letra_digitada
    for letra_secreta in palavra_secreta: 
        print (letras_acertadas)
    else:
        palavra_formada += '*'
    if palavra_formada == palavra_secreta: 
        print ('voce ganhou parabens ')
        print ('a palavra era' ,palavra_secreta)
        print ('tentativas:', numero_tentativas)




