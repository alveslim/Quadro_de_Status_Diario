from datetime import date

data_atual = date.today()
print(data_atual)
data_br = data_atual.strftime('%d/%m/%Y')
print(data_br)
data = '27/07/2026'

if data_br == data:
    print('é hoje')
else:
    print('nao é hoje')