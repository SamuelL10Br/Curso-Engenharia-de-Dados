# Aula 4 - Manipulação de Arquivos (TXT, CSV e JSON)

# --- Criar e escrever em um arquivo TXT ---
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Nome: Samuel\n")
    arquivo.write("Curso: Engenharia de Dados\n")
    arquivo.write("Nota: 9.0\n")

print("Arquivo 'dados.txt' criado com sucesso!")

# --- Ler o conteúdo de um arquivo TXT ---
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:\n", conteudo)

import csv

# --- Ler arquivo CSV ---
with open("alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        print(f"Nome: {linha['nome']} | Curso: {linha['curso']} | Nota: {linha['nota']}")

# --- Escrever um novo arquivo CSV ---
with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    colunas = ["nome", "curso", "nota"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    
    escritor.writeheader()  # Escreve o cabeçalho
    escritor.writerow({"nome": "João", "curso": "Ciência de Dados", "nota": 9.4})
    escritor.writerow({"nome": "Ana", "curso": "Engenharia de Dados", "nota": 8.7})

print("Arquivo 'novos_alunos.csv' criado com sucesso!")

