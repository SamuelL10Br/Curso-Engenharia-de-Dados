# Desafio 3 - Listas e Dicionários
# Lista de alunos (cada um é um dicionário)
alunos = [
    {"nome": "Samuel", "curso": "Engenharia de dados", "nota": 9.0},
    {"nome": "Victor", "curso": "Engenharia de software", "nota": 5.9},
    {"nome": "Maria", "curso": "ADS", "nota": 8.0}
]

# Percorre a lista e mostra os dados de cada aluno
for aluno in alunos:
    print(f"Nome: {aluno["nome"]} | Curso: {aluno["curso"]} | Nota: {aluno["nota"]}")

# Cria uma lista apenas com as notas
notas = [aluno["nota"] for aluno in alunos]

#Calcula a média
media = sum(notas) / len(notas)

#Exibe a média formatada com duas casas decimais
print(f"\nMédia das notas: {media:.2f}")
