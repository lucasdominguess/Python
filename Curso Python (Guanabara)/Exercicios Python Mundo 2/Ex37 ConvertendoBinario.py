num = float (input('digite um numero para conversao '))


print ('[1] Converter para BINARIO \n [2] converter para OCTAL \n [3] converter para HEXADECIMAL ')

opçao = float (input('Digite sua opção de conversao '))


if opçao == 1 : 

    print (f' o numero {num} convertido para BINARIO é {bin(num)}')


elif opçao == 2 : 

    print (f'o numero {num} convertido para OCTAL é {oct(num)}')


elif opçao == 3 : 

    print (f'o numero {num} convertido para HEXADECIMAL é {hex(num)}') 


else: 

    print ('voce nao digitou nenhuma das opçoes listadas acima') 


