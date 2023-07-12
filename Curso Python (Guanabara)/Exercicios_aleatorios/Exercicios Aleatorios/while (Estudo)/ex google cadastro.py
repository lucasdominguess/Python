#cadastrando funcionarios em uma lista
funcionarios = []
adcionar = 1 
while adcionar != 0 : #condição 
    funcionarios.append (input('Digite o nome do funcionario'))
    adcionar = int (input ('Adcionar mais funcionarios? \n Digite [1] para continuar , Digite [0] para parar'))

print (funcionarios)

print (f'Funcionario : ',funcionarios[0])
print (f'Funcionario : ',funcionarios[1])
print (f'Funcionario : ',funcionarios[2])