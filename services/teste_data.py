from datetime import date, timedelta
import pandas as pd
import plotly.express as px

DATA_PATH = "dados/dado.csv"


## -------- Data -------- ##
# Data atual Br
data_atual = date.today()
data_amanha = data_atual + timedelta(days=1)
data_br = data_atual.strftime("%d/%m/%Y")
data_br_amanha = data_amanha.strftime("%d/%m/%Y")

# lendo planilha
df = pd.read_csv(DATA_PATH)
# filtrando apenas planilha de 38000 em diante && data atual
filterdata = df["data_prevista"] == data_br
filterdata_amanha = df["data_prevista"] == data_br_amanha
filterop = df["op"] > 38000
# apresentando o nosso filtro
print(f"\n-------------------- HOJE {data_atual}------------------------\n")
print(f"{df[filterdata & filterop]}")
print(f"\n-------------------- Amanha {data_amanha}------------------------")
print(f"{df[filterdata_amanha & filterop]}\n")
# mostrar quando eh critico (ter um pisca alerta, e mudar para a tela imediatamente)
# mostrar quando finalizado
# um bot q envie no zap (forma de confirma acao para enviar no zap, e enviar no zap)

## -------- Grafico Pizza -------- ##

pizza = px.pie(df, names="cliente")
pizza.show()
# fazer um gradico pizza do ano


## -------- Estatisticas Mensal de Entradas -------- ##
def estatistica_mensal(df, data_atual):
    resultados = []

    for month in range(1, 13):
        # Formata o mês como MM/AAAA
        data_busca = f"{month:02d}/{data_atual.strftime('%Y')}"

        # Conta a quantidade de ocorrências no mês
        total = df["data_prevista"].astype(str).str.contains(data_busca).sum()

        # Guarda o resultado estruturado
        resultados.append({"Mes": f"{month:02d}", "Total": total})

    # Retorna os dados como um DataFrame do Pandas
    return pd.DataFrame(resultados)


# Supondo que você já tenha 'df' e 'data_atual':
df_estatistica = estatistica_mensal(df, data_atual)

# Gera o gráfico de barras/histograma com os dados acumulados por mês
fig = px.bar(
    df_estatistica,
    x="Mes",
    y="Total",
    title=f"Estatística Mensal - {data_atual.strftime('%Y')}",
    labels={"Mes": "Mês", "Total": "Total de Entradas"},
)
fig.show()

## -------- Total de Entradas -------- ##
