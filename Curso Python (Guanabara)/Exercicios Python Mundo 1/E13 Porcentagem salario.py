
S_atual = float (input('qual o valor do salario atual?')) #Vai salvar o valor q digitar
S_aumento = float (input('qual a porcentagem de aumento salarial')) #Salva o valor do desconto

V_doAumento = S_atual*S_aumento/100  #cria variavel , e mostra o valor em R$ baseado na porcentagem

N_salario = S_atual+V_doAumento #valor do salario atual + valor ja convertido na porcentagem 

print (f'com o aumento de {S_aumento:.0f}% , equeivalente a R${V_doAumento:.2f} \no salario atual passara a ser R${N_salario:.2f}') 