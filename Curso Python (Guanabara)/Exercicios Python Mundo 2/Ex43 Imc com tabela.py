totalCompra = float (input('qual total da sua compra '))


print (' digite qual forma de pagamento')

opçoesPag = float (input(' [1] Pagamento a vista\n [2] parcelado cartao 2x \n [3] parcelado em 3x ou mais '))



if opçoesPag == 1 : 

    desconto10 = totalCompra*10/100 

    print (f'sua compra teve 10% de desconto e custara R${totalCompra-desconto10}')

elif opçoesPag ==2 : 

    juros10 = totalCompra*10/100 

    print (f'sua compra teve 10% de juros e custara R${totalCompra+juros10}')

elif opçoesPag == 3: 

    juros20 = totalCompra*20/100 

    print (f'sua compra teve 20% de juros e custara R${totalCompra+juros20}')

