horas = input('Olá, quantas horas você trabalhou esse mês?')
custo = input('Qual o valor em R$ da sua hora?')
try:
    fhoras = float(horas)
except:
    fhoras = -1
try:
    fcusto = float(custo)
except:
    fcusto = -1
if fhoras < 0 :
    print ('Favor informar um valor númerico')
    quit ()
elif fcusto < 0 :
    print ('Favor informar um valor númerico')
    quit ()
elif fhoras > 40 :
    print ('Hora extra')
    horasextra = ((fhoras - 40.0) * (fcusto * 0.5))
    horasregulares = fhoras * fcusto
    pagamento = horasextra + horasregulares
else:
    print ('Hora regular')
    pagamento = fhoras * fcusto
print ('Seu pagamento este mês será de R$', pagamento)