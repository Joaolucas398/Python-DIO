#////////Atividade 1 //////////////////
# a = int(input('Informe um número: '))
#
# div = 0
#o range diz ate onde vai o laço
# for x in range(1, a+1):
#     resto = a % x
#     print (x, resto)
#     if resto == 0:
#         div += 1
#
# if div ==2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))

#/////////////////////Atividade 2/////////////////////////////


# for i in range(101):
#     div = 0
#     for x in range(1, i+1 ):
#         resto = i % x
#         #print (x, resto)
#         if resto == 0:
#             div += 1
#
#     if div ==2:
#         print(i)

#///////// atividade 3

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

#/////////////////atividade 4

a = int(input('Informe a primeira nota: '))
while a > 10:
    a = int(input('Nota incorreta, informe uma nota valida: '))

b = int(input ('Informe a segundo nota: '))
while b > 10:
    b = int(input('Nota incorreta, informe uma nota valida: '))

c = int(input('Informe a terceiro nota:' ))
while c > 10:
    c = print('Nota incorreta, informe uma nota valida: ')

d = int(input('Informe a terceiro nota:' ))
while d > 10:
    d = int(input('Nota incorreta, informe uma nota valida: '))

media = (a+b+c+d)/4
print('A media do aluno é {}'.format(media) )

