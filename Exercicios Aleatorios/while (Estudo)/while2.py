frase = 'apredendo a linguagem de programação python em dois mil e vinte e tres' 
qtds_apareceu_mais_vezess =0 
letra_apareceu_mais_vezes = ''
i = 0 

while i < len(frase): 
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qlts = frase.count(letra_atual)

    if qtds_apareceu_mais_vezess < letra_atual:
        qtds_apareceu_mais_vezess= letra_atual
        letra_apareceu_mais_vezes = letra_atual

    print (letra_atual , qlts) 
    i +=1 

print (f'a letra que apareceu mais vezes foi {letra_apareceu_mais_vezes}
ela apareceu {qtds_apareceu_mais_vezess}')
