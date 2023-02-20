entrada = input("Digite uma lista de números inteiros separados por espaços: ")
numeros = entrada.split() # separa a string nos espaços em branco

soma_pares = 0
for um in numeros:
    if int(um) % 2 == 0: # verifica se o número é par
        soma_pares += int(um) # soma o número à variável de soma dos pares

print("A soma dos números pares é:", soma_pares)
