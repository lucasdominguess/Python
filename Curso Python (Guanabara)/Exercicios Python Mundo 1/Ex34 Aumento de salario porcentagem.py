salario = float (input('digite o seu salario '))
aumento15 = salario*15/100
aumento10 = salario*10/100 
if salario <= 2000 : 
    print (f'seu salario tera o aumento de 15% e passara a ser {salario+aumento15:.2f}') 

elif salario >2000 : 
    print (f'seu salario tera o aumento de 10% e passara a ser {salario+aumento10:.2f}')


