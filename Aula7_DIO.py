class Calculadora:
    def __init__(self,num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    # Definições

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


Calculadora = Calculadora(10,2)
print(Calculadora.valor_a)
print(Calculadora.soma())
print(Calculadora.subtracao())
print(Calculadora.multplicacao())
print(Calculadora.divisao())
