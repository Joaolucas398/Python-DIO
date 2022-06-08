a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao =  a * b
divisao = a / b
resto = a % b

#print (type(soma)) o type serve para saber que tipo é a variavel selecionada
#e para converter uma variavel inteira para string utiliza-se o "str"
soma = str(soma)
# outra forma:
#print('a soma é: ' + str(soma))
#o Format é a melhor opção pois ele converte independente do tipo de variavel
print('soma: {}'.format(soma))
print('a soma é: {soma}\n'
      ' e a subtração é: {subtracao}\n'
      ' a multplicação é: {mult}\n'
      ' a divisão é {divisao}\n'
      ' o resto é {resto}'.format(soma = soma, subtracao=subtracao,
                                  mult = multiplicacao, divisao = divisao,resto = resto))
print (soma)
print (subtracao)
print (multiplicacao)
#mais um exemplo de conversão
print (int(divisao))
print(resto)


print('Interação com o usuario')
print('Informe seu peso e sua altura pra calcular seu IMC')
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso/(altura*altura)
print('imc é {}'.format(imc))
