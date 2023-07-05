produto = float (input('Digite o valor do produto'))
desconto = float (input('Digite a porcentagem do desconto'))

valor = produto*desconto/100
Nvalor = produto-valor 
print (f'o produto custa R${produto:.2f} , mas com o desconto de {desconto:.0f}% custara R${Nvalor:.2f}')
