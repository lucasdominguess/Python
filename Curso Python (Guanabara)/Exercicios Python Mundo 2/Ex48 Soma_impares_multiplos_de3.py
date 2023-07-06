#somar numeros impares , multiplos de 3 entre 1 a 500 
contador= 0
soma= 0
for item in range (1,101,2): 
    if item % 3==0: # se resto da divisao por 3 for 0
        contador= contador+1 #Acumulador de todos os itens validados no if 
        soma=soma+item #soma dos valores atuais + valores adcionados
        
 
print (contador)
print (soma)