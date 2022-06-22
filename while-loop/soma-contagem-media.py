soma = 0.0
contagem = 0.0
while True :
    numero = input ('Enter a number: ')
    if numero == 'done' :
        break
    try:
        numeroint = float (numero)
    except:
        print ('Invalid input')
        continue
    soma = soma + numeroint
    contagem = contagem + 1
print ('Soma:', soma, '\nNúmero de itens:', contagem, '\nMédia:', soma/contagem)