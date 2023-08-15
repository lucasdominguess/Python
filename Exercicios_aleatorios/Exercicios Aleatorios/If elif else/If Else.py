nome = str (input('qual é seu nome? ')).strip()
if nome == 'lucas':
    print ('que nome lindo')
elif nome == 'maria ' or nome== 'joao' or nome== 'leoan':
    print ('seu nome e muito popular')
elif nome in 'ana claudia sabrina jessica':
    print ('nome de mulher')
else:
    print ('que nome feio')


