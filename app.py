from datetime import date
import pandas as pd

data_atual = date.today()
# print(data_atual)
data_br = data_atual.strftime("%d/%m/%Y")
# print(data_br)
data = "27/07/2026"
df = pd.read_csv("dado.csv")
filterdata = df["data_prevista"] == data_br
filterop = df["op"] > 38000
print(df[filterdata & filterop])
