'''Escreva um programa que recebe uma lista de números inteiros do usuário e, em seguida,
 calcula e imprime a média desses números. Use um loop while para receber entrada do usuário até que eles digitem "fim". 
Use um loop for para iterar sobre a lista e calcular a média.'''


lista = []
parar = 0

while parar <6 : 
     lista.append(int(input('Digite ate 5 numeros aleatorios')))
     qtd_numeros =(len(lista))
     soma_dos_numeros = (sum(lista)) #soma dos numeros da lista 
     media = soma_dos_numeros/qtd_numeros
     parar+=1

print (f'a lista digitada foi ', lista)

print (f'a media dos numeros digitados foi {media:.2f}')

numeros = []
entrada = input("Digite um número inteiro (ou 'fim' para sair): ")

while entrada != "fim":
    numero = int(entrada)
    numeros.append(numero)
    entrada = input("Digite um número inteiro (ou 'fim' para sair): ")

soma = sum(numeros)
media = soma / len(numeros)

print(f"A média dos números é: {media}")


