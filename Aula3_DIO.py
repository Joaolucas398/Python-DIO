#/////////// terceira atividade ///////////
aluno= input('Informe o nome do aluno: ')
a = int(input('Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))

media = (a+b+c+d)/4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('A media do aluno ' + aluno + ' é: {}'.format(media))
else:
    print('Foi informado alguma nota errada')

#////////////////////// segunda atividade ///////////////

# a = int(input('Informe um valor: '))
# b = int(input('Infome um segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# # or quer dizer 'ou' pode se usar o 'not' para inverter a logica do operador logico
# if resto_a == 0 or resto_b == 0:
#     print('Apenas números pares foram informados!')
# else:
#     print('Apenas números impares foram informados!')

#/////////////////////////////Primeira atividade//////////////////////////////////////////////

# a = int(input ('Informe o primeiro valor: '))
# b = int(input ('Informe o segundo valor: '))
# c = int(input('Informe o terceiro valor:' ))
# and quer dizer '&&'
# if a > b and a > c:
#     print('O maior número é A {}'.format(a))
# #o elif é o "elseif"
# elif b > a and b > c:
#     print('O maior número é B {}'.format(b))
# else:
#     print('O maior número é C {}'.format(c))
#
# print('Programa finalizado')