import pandas as pd

# Lendo o arquivo CSV criado no desafio anterior
df = pd.read_csv("desafio4.csv", encoding="utf-8")

# Exibindo o DataFrame completo
print("=== TABELA COMPLETA ===")
print(df)

# Exibindo apenas os nomes
print("\n=== SOMENTE NOMES ===")
print(df["nome"])

# Exibindo estatísticas das notas
print("\n=== ESTATÍSTICAS DAS NOTAS ===")
print(df["nota"].describe())

# Filtrando alunos com nota acima de 8
print("\n=== ALUNOS COM NOTA >= 8 ===")
print(df[df["nota"] >= 8])

print("\n=== ALUNOS ORDENADOS POR NOTA ===")
print(df.sort_values(by="nota", ascending=False))

print("\n=== APENAS QUEM FAZ ENGENHARIA DE DADOS ===")
print(df[df["curso"] == "Engenheiro de Dados"])
