'''Crie um programa que leia um numero real qlq e mostre sua sua porçao inteira'''
#essa formula nao mostra inteiro 
num = float (input('Digite um numero'))

print (f'a porçao inteira do numero {num} é {num:.0f}') #Forma errada!

#Exemplo 2 
import math  #Importando a biblioteca math 
from math import trunc #importanto a funçao trunc da biblioteca math 

num = float (input('Digite um numero')) 
print (f'a porçao inteira do numero {num} é {int(num)}') #pode usar tbm funçao int em vez de trunc