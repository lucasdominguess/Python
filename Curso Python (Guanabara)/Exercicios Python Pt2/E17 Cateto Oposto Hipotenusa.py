'''faca um programa que mostre'''

Co = float (input('qual medida do cateto Oposto'))
Cad = float(input('qual medida do cateto adjacente'))

Hipo = (Co**2+Cad**2)**(1/2) 

print (f'a hipotenusa vai medir {Hipo:.2f}') 

import math 
hip = math.hypot(Co,Cad) #funlao que qualcula a hipotenusa 

print (hip)