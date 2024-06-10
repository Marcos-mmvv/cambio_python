from forex_python.converter import CurrencyRates

print(f'{'-'*30} CONVERSOR DE MOEDA EM TEMPO REAL {'-'*30}\n')

valor = str(input('Informe o valor da moeda a ser convertida: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Informe a moeda de origem: ').upper()
moeda_destino = input('Informe a moerda de destino: ').upper()

# Realiza a conversão de acordo com a taxa do câmbio do dia
Result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

#Resultado da conversão
print(f'$ {valor:,.2f} {moeda_origem:,.2f} = $ {Result:,.2f} {moeda_destino:,.2f}.')




