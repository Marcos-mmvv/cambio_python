#Cotação internacional
from forex_python.converter import CurrencyRates

#Exibir a barra
from tqdm import tqdm

#Tempo
import time

# importa função de data
from datetime import date

# Calendário
dia = date.today().day
mes = date.today().month
ano = date.today().year

#Exibir capa
print(f'{'-'*30} |CONVERSOR DE MOEDA EM TEMPO REAL| {'-'*30}')
print(f'\n{'=' * 40} {dia}/{mes}/{ano} {'=' * 45}\n')

#Variáveis
valor = str(input('Informe o valor da moeda a ser convertida: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Informe a moeda de origem: ').upper()
moeda_destino = input('Informe a moerda de destino: ').upper()

# Realiza a conversão de acordo com a taxa do câmbio do dia
Result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

#Resultado da conversão
for i in tqdm(range(100)):
    time.sleep(0.01)
print(f'$ {valor:,.2f} {moeda_origem:,.2f} = $ {Result:,.2f} {moeda_destino:,.2f}.')




