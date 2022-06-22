str = 'X-DSPAM-Confidence:0.8475'
encontre_o_caracter = str.find (':')
numero_desejado = str[encontre_o_caracter + 1: ]
final_exercicio = float (numero_desejado)
print (final_exercicio)
print (final_exercicio + 42.0)