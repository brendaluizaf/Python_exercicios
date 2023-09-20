nome=str(input("QUAL O SEU NOME? "))
idade=int(input("QUAL SUA IDADE? "))

print("BEM- VINDO {}! VOCÊ TEM {} ANOS.".format(nome,idade))

numero=int(input("DIGITE UM NÚMERO: "))
numero1=int(input("DIGITE OUTRO NÚMERO: "))
soma= numero + numero1

print("A SOMA DESSES NÚMEROS SÃO: {}".format(soma))

def fatorial(n):
    if n < 0:
        return "O fatorial não está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso:
numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')

a=int(input("Digite o número para a operação: "))
b=int(input("Digite outro número para a operação: "))

class Calculadora:
    def soma(self, a, b):
        return a + b

    def multiplicacao(self, a, b):
        return a * b

# Exemplo de uso:
calculadora = Calculadora()

resultado_soma = calculadora.soma(a, b)
print(f"A soma é: {resultado_soma}")

resultado_multiplicacao = calculadora.multiplicacao(a, b)
print(f"A multiplicação é: {resultado_multiplicacao}")
