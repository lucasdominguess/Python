
'''
for c in range(0,3): 
    numero = int (input('digite um numero')) #linha de comando dentro do range 
    #ira excutar esse comando 3 vezes 

print ('fim')
'''

Total_notas = 0 

for n in range(0,4): #excutar o comando 4 vezes
    nota = int (input('Quanto foi sua nota na prova?'))
    Total_notas+=nota #soma cada valor digitado a valor da nota anterior

print (f'A somatoria das notas foi {Total_notas}')
print (f'sua media ficou em {Total_notas/10}')