from datetime import date, timedelta
import pandas as pd

# Data atual Br
data_atual = date.today()
data_amanha = date.strftime(d)
data_br = data_atual.strftime("%d/%m/%Y")
# lendo planilha
df = pd.read_csv("dado.csv")
# filtrando apenas planilha de 38000 em diante && data atual
filterdata = df["data_prevista"] == data_br
filterdata = df["data_prevista"] == data_br
filterop = df["op"] > 38000
# apresentando o nosso filtro
print(f"-------------------- HOJE {data_atual}------------------------")
print(df[filterdata & filterop])
print(f"-------------------- HOJE {data_atual}------------------------")
