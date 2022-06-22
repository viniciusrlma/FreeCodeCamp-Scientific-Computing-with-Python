arquivo = input ('Informe o nome de um arquivo: ')
abrir_arquivo = open(arquivo)

dicionário = dict()
for linhas in abrir_arquivo:
    linhas = linhas.rstrip()
    splitando = linhas.split()
    for palavras in splitando:
        dicionário[palavras] = dicionário.get(palavras,0)+1
lista = sorted([(valor,chave) for chave,valor in dicionário.items()], reverse=True)

for valor, chave in lista[:10]:
    print (chave, valor)
