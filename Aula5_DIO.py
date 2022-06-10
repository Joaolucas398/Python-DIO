lista = [1,3,5,7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# print(lista_animal)
#sort ordena a lista
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)

tupla = (1,10,12,14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple (lista_animal)
print(type(tupla_animal))
lista_numerica = list(tupla)
print(type (lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(max(lista))
#
# verificando se tem um valor ou nome na lista

# if 'lobo' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('Não existe um gato na lista')
# #append inclui novas valores ou String na lista
#     lista_animal.append('lobo')
#     print(lista_animal)

#o pop retira a ultima posição da lista e vc tbm pode passar qual posição retirar
# lista_animal.pop()
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)