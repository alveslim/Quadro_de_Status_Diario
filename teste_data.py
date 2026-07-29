from datetime import date, timedelta

data_atual = date.today()
data_amanha = data_atual + timedelta(days = 1)
data_br = data_atual.strftime("%d/%m/%Y")
data_br_amanha = data_amanha.strftime("%d/%m/%Y")
print(data_br)
print(data_br_amanha)
data = "30/07/2026"

if data_br == data:
    print("é hoje")
else:
    print("nao é hoje")
