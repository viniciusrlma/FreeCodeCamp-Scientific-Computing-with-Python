hor = input('Olá, quantas horas você trabalhou esse mês?')
cus = input('Qual o valor em R$ da sua hora?')
fhor = float(hor)
fcus = float(cus)
if fhor > 40 :
    print ('Hora extra')
    he = ((fhor - 40.0) * (fcus * 0.5))
    hr = fhor * fcus
    pag = he + hr
else:
    print ('Hora regular')
    pag = fhor * fcus
print ('Seu pagamento este mês será de R$', pag)