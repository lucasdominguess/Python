
nome = str (input('Digite seu nome completo ')).strip()



print ('Seu nome tem silva? {}'.format('SILVA' in nome.upper().strip())) #format string antiga 
print (f"Seu nome tem silva?{'SILVA' in nome.upper().strip()}") # nesse caso usar aspas duplas para f-string