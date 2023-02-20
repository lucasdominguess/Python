'''lista1 = [] #criar lista vazia 
num = 0 

while num <= 4: 
    lista1.append(input('digite seu nome'))
    num+=1
  
print (' os nomes digitados foram ', lista1)
'''
lista1 = [] #criar lista vazia 
num = 0 
continuar = 'SIM'
while continuar == 'SIM' or num <= 4: 
        lista1.append(input('digite seu nome'))
        num+=1
        continuar = input('Deseja adcionar mais algum nome? S/N?').upper().strip()
        
    
print (' os nomes digitados foram ', lista1) 