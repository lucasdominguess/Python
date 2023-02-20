'''adcionando * na frase '''
#adcina algo entre as letras 

nome = 'luiz otavio' 

indice = 0 
novo_nome = ''
while indice < len(nome):
    letra =nome[indice]
    novo_nome += f'*{letra}' #adcina algo entre as letras  
 
    indice+=1 

print (novo_nome)
#>> *l*u*i*z* *o*t*a*v*i*o #saida