valorDaCasa = int (input('qual o valor do imovel para financiamento'))
valorSalario = int (input('qual o valor do salario'))
anosFinanciamento = int (input('quanto anos deseja quitar o imovel '))
meses = anosFinanciamento*12 #retorna a qualtidade de meses 
valorParcela = valorDaCasa/meses

if valorParcela > valorSalario*30/100 : #verifica se a parcela excede os 30% do salario
    print (f'emprestimo negado')
    print (f'o valor da parcela seria de {valorParcela:.2f}')
    print (f' pois 30% do salario sera de : {valorSalario*30/100:.2f}')
else : #caso nao exceda ...
    print (f'emprestimo aprovado!\n valor da parcela sera de {valorParcela} \n e nao excede os 30% do salario' )
    print (valorSalario*30/100) 