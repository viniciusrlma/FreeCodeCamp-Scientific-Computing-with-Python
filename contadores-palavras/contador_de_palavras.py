texto = input ('Insira uma linha de texto: ')
palavras_identificadas = texto.split()
print ('Palavras identificadas:', palavras_identificadas)

contagem = dict()
print ('Contando...')
for contabilização_de_palavras in palavras_identificadas :
    contagem[contabilização_de_palavras] = contagem.get(contabilização_de_palavras,0)+1
print ('Frequência das palavras: ', contagem)
print (list(contagem))