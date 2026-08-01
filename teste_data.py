from datetime import date, timedelta
import calendar
import pandas as pd
import plotly.express as px

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
# print(total_hevi)
print("--------------------------------------------------------------")
print(df["cliente"].value_counts())  # contagem de todos os clientes de uma vez
print("--------------------------------------------------------------")

## -------- Estatisticas Mensal -------- ##

for mouth in range(1, 13):
    # Using f-string to format month and year (%Y)
    data = f"{mouth:02d}/{data_atual.strftime('%Y')}"
    print(data)
    contagem = df["data_prevista"].str.contains(data).sum()
    print(contagem)
    dado = df["data_prevista"].str.lower().str.contains(data).sum()
    print(f"total de entradas: {dado}\n")

## -------- Calendario -------- ##

ano_atual = calendar.calendar(2026)
# print(ano_atual)
ano_atual = date.today().year
print(ano_atual)
ano_passado = ano_atual - 1
print(ano_passado)

## -------- Grafico -------- ##

pizza = px.pie(df, names="cliente")
pizza.show()

histograma = px.histogram(dado, y="data_prevista", x="")
histograma.show()
