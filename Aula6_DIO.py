# um conjunto caracterizado pelos {} não permite duplicidade.
conjunto = {1,2,3}
conjunto2 = {3,4,5,6}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}' .format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}' .format(conjunto_interseccao))

conjunto_diferenca = conjunto.difference(conjunto2)
print ('Diferença entre 1 e 2: {}' .format(conjunto_diferenca))

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}' .format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('B é um superconjunto de A: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}' .format(conjunto_superset))


lista = ['cachorro','cachorro','gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


# conjunto.add(4)
# conjunto.discard(2)
# print(conjunto)