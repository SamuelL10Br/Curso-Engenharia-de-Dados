import csv
with open('desafio4.csv',"w",encoding="utf-8") as desafioCSV:
    colunas = ["nome","curso","nota"]
    escritor = csv.DictWriter(desafioCSV,fieldnames=colunas)

    escritor.writeheader()
    escritor.writerow({"nome":"Samuel","curso":"Engenheiro de Dados","nota":9.0})
    escritor.writerow({"nome":"Maria","curso":"ADS","nota":8.2})
    escritor.writerow({"nome":"Victor","curso":"Engenheiro de Software","nota":7.5})
print("Arquivo 'desafio4' foi gerado com sucesso!") 

with open("desafio4.csv", "r", encoding="utf-8") as leitura:
    leitor = csv.DictReader(leitura)

    alunos = list(leitor)  # convertendo o leitor para lista (agora podemos usar várias vezes)

# Exibindo os dados
for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Curso: {aluno['curso']} | Nota: {aluno['nota']}")

# Pegando somente as notas e convertendo para número
notas = [float(aluno["nota"]) for aluno in alunos]

# Calculando a média
media = sum(notas) / len(notas)

print(f"\nMédia das notas: {media:.2f}")

# Para arquivos do tipo JSON
import json
resultado = {
    "media_geral": round(media, 2),   # duas casas decimais
    "total_alunos": len(alunos)
}

with open("resultado.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=4)

print("Dados salvos em resultado.json")
