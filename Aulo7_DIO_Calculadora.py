class Calculadora:


    # Definições

    def soma(self ,valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self ,valor_a, valor_b):
        return valor_a - valor_b

    def multplicacao(self ,valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self ,valor_a, valor_b):
        return valor_a / valor_b


Calculadora = Calculadora()

print(Calculadora.soma(10,2))
print(Calculadora.subtracao(100,5))
print(Calculadora.multplicacao(5,5))
print(Calculadora.divisao(12,2))
