def mensagem(txt):

    print ('---'*20)

    print(txt)

    print ('---'*20)



def soma(*valores):  # cria funçao sem saber qtd de caracteres que ira receber 

    s=0 

    for num in valores: 

        s+=num

    print (f'a soma dos valores {valores} temos {s}') 


'''soma (2,4,5)

soma (9,4,8,1)'''


def tabuada (num=1): 

    for n in range (11):

        print(f'{num} x {n} = {num*n}')
        return n


f1= tabuada (float(input ('digite um numero')))

f2= tabuada (float(input('digite outro numero')))

f3= tabuada (float(input('digite o ultimo numero')))


print (f'os valores sao {f1} , {f2} , {f3}')