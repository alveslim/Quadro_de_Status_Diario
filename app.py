from datetime import date

data_atual = date.today()
# print(data_atual)
data_br = data_atual.strftime("%d/%m/%Y")
# print(data_br)
data = "27/07/2026"
with open("dado.csv", "r", encoding="utf-8") as file:
    for line in file:
        op, cliente, empresa, status, data_prevista = line.rstrip().split(",")
        print(f"OP: {op} - Cliente: {cliente} | {empresa} {status}, {data_prevista}")

    for line in file:
        if data_prevista == data_br:
            print("é hoje")
        else:
            print("nao é hoje")
