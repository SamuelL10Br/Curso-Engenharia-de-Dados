#Aula 2 - Tipos de dados e operações
#Variáveis com diferentes tipos

nome = "Samuel"  #str (texto)
idade = 22  #int (número inteiro)
altura = 1.78  #float(número decimal)
estudando = True  #bool (verdadeiro ou falso)

#Exibindo o tipo de cada variável
print("Tipo da variável nome:", type(nome))
print("Tipo da variável idade:", type(idade))
print("Tipo da variável altura:", type(altura))
print("Tipo da variável estudando:", type(estudando))

#Operações matemáticas
a = 10
b = 8
print("Adição: ", a + b)
print("Multiplicação: ", a * b)
print("Subtração: ", a - b)
print("Divisão: ", a / b)
print("Divisão inteira: ", a // b)
print("Resto da Divisão: ", a % b)
print("potência: ", a ** b)

#Conversão de tipos
idade = int(input("Digite sua idade: "))
ano_atual = 2025
ano_nascimento = ano_atual - idade

print("Você nasceu em", ano_nascimento)