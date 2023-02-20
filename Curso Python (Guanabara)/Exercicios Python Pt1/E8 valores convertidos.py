'''escreva um progrma que leia um valor em metros e exiba convertidos em centimetros e milimetros '''

medida = float (input('Digite uma distancia em metros '))

cm = medida *100 
mm = medida*1000 

print (f' a distancia {medida}Km , equivale a {cm:.0f} centimetros e tbm {mm:.0f} milimetros') 