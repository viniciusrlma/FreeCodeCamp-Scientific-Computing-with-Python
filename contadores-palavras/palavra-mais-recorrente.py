nome_do_arquivo = input ('Insira o nome de um arquivo: ')
abrir_arquivo = open(nome_do_arquivo)

contagem_de_palavras = dict()
for linhas in abrir_arquivo: 
    linhas = linhas.rstrip()
    splitando_palavras = linhas.split()
    for palavras in splitando_palavras:
        contagem_de_palavras[palavras] = contagem_de_palavras.get(palavras,0)+1

numero_de_aparicoes = None
palavra_mais_recorrente = None
for k,v in contagem_de_palavras.items():
    if numero_de_aparicoes is None or v > numero_de_aparicoes:
        numero_de_aparicoes = v
        palavra_mais_recorrente = k

print ('Palavra mais recorrente:', palavra_mais_recorrente, '\nNúmero de aparições:', numero_de_aparicoes)
