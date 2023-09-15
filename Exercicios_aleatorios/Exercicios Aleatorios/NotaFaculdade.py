

a1 = float (input('Primeira nota '))
a2 = float (input('segunda  nota '))
a3 = float (input('Terceira nota '))
a4 = float (input('Quarta nota '))

somant = a1+a2+a3+a4 

divnt4 = somant /4 
Nota_Final =divnt4*0.4 
n2 =6-Nota_Final 
n2_final = n2 /0.6


print (f'soma das notas : {somant} \n nota dividida por 4 : {divnt4} \n Nota Final : {Nota_Final:.2f}')
print (f'Sua nota N2 Precisa ter no minimo: {n2_final:.2f} \n Para depos da Conversao ficar com: {n2:.2f}')