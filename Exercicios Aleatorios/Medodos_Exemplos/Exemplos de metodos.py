len() - retorna o tamanho de uma sequência (por exemplo, lista, tupla, string).
print(len([1, 2, 3]))       # Saída: 3
print(len("Python é legal!"))  # Saída: 16

max() - retorna o valor máximo em uma sequência.
print(max([1, 2, 3, 4, 5]))       # Saída: 5
print(max("Python é legal!"))  # Saída: "y"

min() - retorna o valor mínimo em uma sequência.
print(min([1, 2, 3, 4, 5]))       # Saída: 1
print(min("Python é legal!"))  # Saída: " "

sum() - retorna a soma dos valores em uma sequência.
print(sum([1, 2, 3, 4, 5]))       # Saída: 15

sorted() - retorna uma lista ordenada.
print(sorted([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Saída: [1, 1, 2, 3, 4, 5, 5, 6, 9]

reversed() - retorna uma sequência em ordem inversa.
print(list(reversed([1, 2, 3, 4, 5])))         # Saída: [5, 4, 3, 2, 1]
print("Python é legal!"[::-1])  # Saída: "!lagel é nohtyP"

type() - retorna o tipo de um objeto.
print(type("Python"))        # Saída: <class 'str'>
print(type([1, 2, 3, 4, 5]))  # Saída: <class 'list'>

any() - retorna True se pelo menos um elemento de uma sequência é True.
print(any([False, False, True]))       # Saída: True
print(any([0, 0, 0]))  # Saída: False

all() - retorna True se todos os elementos de uma sequência são True.
print(all([True, True, True]))       # Saída: True
print(all([True, False, True]))  # Saída: False

enumerate() - retorna uma tupla com um índice e um valor correspondente de uma sequência.
print(list(enumerate([1, 2, 3])))       # Saída: [(0, 1), (1, 2), (2, 3)]

zip() - combina duas ou mais sequências em tuplas de pares correspondentes.
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))       # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]

map() - aplica uma função a cada elemento de uma sequência.
print(list(map(lambda x: x * 2, [1, 2, 3])))       # Saída: [2, 4, 6]

filter() - retorna uma sequência filtrada contendo apenas elementos que atendem a uma condição.
print(list(filter(lambda x: x > 2, [1, 2, 3, 4, 5])))       # Saída: [3, 4, 5]

join() - combina uma sequência de strings em uma única string usando um separador.
print(' '.join(['Python', 'é', 'legal!']))       # Saída: 'Python é legal!'

:.2f = o Python vai entender que quer duas casas decimais após o ponto. Se usar %. 1f, o Python exibe só uma casa decimal