'''Crie um programa que pede para o usuário digitar uma sequência de números inteiros, 
um de cada vez. O programa deve continuar pedindo números até que o usuário digite a palavra
 "fim". Depois disso, o programa deve imprimir o maior número da lista.'''

numeros = []

entrada = (input('Digite um numero ou [sair] para sair do programa')) 


while entrada != 'sair': 
    numero = (int(entrada)) #convertendo numero string para inteiro
    numeros.append(numero) #adcionando numero 
    entrada = (input('Digite um numero ou digite sair para sair do programa'))

print ('o maior numero digitado foi ',(max(numeros))) 
print ('o maior numero digitado foi ' ,(min(numeros))) 

#Gpt
numeros = []
entrada = ""

while entrada != "fim":
    entrada = input("Digite um número inteiro (ou 'fim' para sair): ")
    if entrada != "fim":
        numeros.append(int(entrada))

if numeros:
    maior = max(numeros)
    print(f"O maior número é: {maior}")
else:
    print("Nenhum número foi digitado.")
'''Neste programa, criamos uma lista vazia chamada numeros 
e usamos um loop while para receber entrada do usuário até que eles digitem "fim". 
Dentro do loop, convertemos a entrada do usuário em um número inteiro usando a função int() 
e adicionamos o número à lista numeros. Quando o usuário digita "fim", saímos do loop
 e usamos a função max() para encontrar o maior número na lista,
  que é armazenado na variável maior. Se a lista estiver vazia, imprimimos uma mensagem informando que nenhum número foi digitado.'''