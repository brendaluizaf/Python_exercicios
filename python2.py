nome = "Brenda"
print(nome)
idade = input("Digite sua idade: ")
idade = int(idade)
for i in range(1, 11):
    print(i)
for i in range(2, 11, 2):
    print(i)
for i in range(1, 11, 2):
    print(i)
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
def eh_par(numero):
    return numero % 2 == 0

