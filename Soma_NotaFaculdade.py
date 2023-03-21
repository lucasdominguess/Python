
notas = [] 

for n in range (0,4) : 
    nota_AT = float (input('Digite a nota da atividade')) 
    notas.append(nota_AT)
soma_atv = sum(notas)
Total_ativ_Div4 = soma_atv/4
nota_atv_final = Total_ativ_Div4*0.4 
#print (Total_ativ_Div4)
print (f'O resultado final das suas atividades é {nota_atv_final:.2F}')

''''nota_prova = float (input('Digite a nota tirada na N2 Prova final '))
nota_prova_final= nota_prova*0.6 
print (nota_prova_final)
'''
#print (nota_prova_final+nota_atv_final)
'''exemplo nota das atividades 
soma das notas e divide por 4  
resultado disso faça vezes 0,4 '''