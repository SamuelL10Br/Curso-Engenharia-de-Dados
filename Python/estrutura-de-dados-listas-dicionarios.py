#Criando uma lista de linguagens
linguagens = ["Python", "SQL", "Java", "C++"]
print("Linguagens de programação:",linguagens)

#Acessando itens da lista
print("Primeira linguagem:",linguagens[0]) #Mostra "Python"
print("Última linguagem:",linguagens[-1]) #Mostra "C++"

#Adicionando novo item
linguagens.append("Go") #Adiciona no final

#Removendo item
linguagens.remove("Java") #tira um item específico

#Alterando valor
linguagens[1] = "SQL Server" #Altera o valor da posição 1
print("Lista atualizada");

#Percorrendo listas com for
print("Listando as linguagens:")
for linguagem in linguagens:
 print("-", linguagem)

#Explicação: o laço for percorre cada item da lista, um por um.
#Isso será essencial quando você estiver lendo linhas de um arquivo CSV
#Ou registros de banco de dados.

#Criando um dicionário
pessoa = {                                #Um dicionário guarda partes de chave e valor.                                  
 "nome": "Samuel",                        #Perfeito para representar informações estruturadas
 "idade": 22,                             #Como dados de uma pessoa, produto, aluno e etc.
 "profissao": "Engenheiros de Dados"        
}
print(pessoa)
print("Nome", pessoa["nome"])
print("Profissão:", pessoa["profissao"])

#Modificando dicionários

#Adicionando nova chave
pessoa["cidade"] = "Lisboa"

#Alterando valor
pessoa["idade"] = 23

#Removendo chave
del pessoa["profissao"]

print("Dicionário atualizado:", pessoa)


#Dicionário dentro de lista(estrutura mista)
#Esse formato é extremamente comum em Engenharia de dados
#Pois é como os dados vêm de APIS e arquivos JSON.

#Lista de dicionários (vários registros)
pessoas = [
 {"nome": "Samuel", "idade": 22},
 {"nome": "Maria", "idade": 25},
 {"nome": "João", "idade": 30}
]

for pessoa in pessoas:
 print(pessoa["nome"], "tem", pessoa["idade"], "anos")

