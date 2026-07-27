from datetime import date

with open("dado.csv", "r", encoding="utf-8") as file:
    for line in file:
        op, cliente, empresa, status, data_prevista = line.rstrip().split(",")
        print(f"OP: {op} - Cliente: {cliente} | {empresa} {status}, {data_prevista}")