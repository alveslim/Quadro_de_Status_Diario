from datetime import date, timedelta
import pandas as pd

## -------- Data -------- ##
# Data atual Br
data_atual = date.today()
data_amanha = data_atual + timedelta(days=1)
data_br = data_atual.strftime("%d/%m/%Y")
data_br_amanha = data_amanha.strftime("%d/%m/%Y")

# lendo planilha
df = pd.read_csv("dado.csv")
# filtrando apenas planilha de 38000 em diante && data atual
filterdata = df["data_prevista"] == data_br
filterdata_amanha = df["data_prevista"] == data_br_amanha
filterop = df["op"] > 38000
# apresentando o nosso filtro
print(f"\n-------------------- HOJE {data_atual}------------------------\n")
print(f"{df[filterdata & filterop]}")
print(f"\n-------------------- Amanha {data_amanha}------------------------")
print(f"{df[filterdata_amanha & filterop]}\n")

## -------- Estatisticas --------  ##
total_hevi = (df["cliente"] == "hevi").sum()
print(total_hevi)

print(df["cliente"].value_counts())  # contagem de todos os clientes de uma vez
