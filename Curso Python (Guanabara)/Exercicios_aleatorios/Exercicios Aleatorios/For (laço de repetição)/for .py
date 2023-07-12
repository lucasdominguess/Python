#iteravel entrega um valor por vez 

texto = 'python'
novo_texto = ''
for letra in texto : #Para cada letra no texto faça:
    print (letra)
    novo_texto+= f'*{texto}'

print (novo_texto)