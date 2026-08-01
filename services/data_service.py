from datetime import date, timedelta
import pandas as pd
import plotly.express as px

DATA_PATH = "dados/dado.csv"


def carregar_dados():
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        return pd.DataFrame()


def obter_dados_dashboard():
    df = carregar_dados()
    if df.empty:
        return {
            "hoje": [],
            "amanha": [],
            "data_hoje": "",
            "data_amanha": "",
            "tem_critico": False,
        }

    data_atual = date.today()
    data_amanha = data_atual + timedelta(days=1)

    data_br = data_atual.strftime("%d/%m/%Y")
    data_br_amanha = data_amanha.strftime("%d/%m/%Y")

    filterop = df["op"] > 38000

    df_hoje = df[(df["data_prevista"] == data_br) & filterop].copy()
    df_amanha = df[(df["data_prevista"] == data_br_amanha) & filterop].copy()

    # REGRA CRÍTICA: Marca como 'critico' se o status for 'critico' ou 'avaliacao'
    # Ajuste essa condição conforme a sua lógica do negócio
    df_hoje["critico"] = df_hoje["status"].str.lower().isin(["critico", "atrasado"])

    tem_critico = df_hoje["critico"].any()

    return {
        "hoje": df_hoje.to_dict(orient="records"),
        "amanha": df_amanha.to_dict(orient="records"),
        "data_hoje": data_br,
        "data_amanha": data_br_amanha,
        "tem_critico": tem_critico,
    }


def gerar_grafico_pizza_html():
    df = carregar_dados()
    if df.empty:
        return ""
    fig = px.pie(df, names="cliente", title="Distribuição por Cliente")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


def gerar_grafico_pizza_html():
    df = carregar_dados()
    if df.empty:
        return ""
    fig = px.pie(df, names="cliente", title="Distribuição por Cliente")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=35, b=20),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
        ),  # Legenda na horizontal topo
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


def gerar_grafico_mensal_html():
    df = carregar_dados()
    if df.empty:
        return ""

    data_atual = date.today()
    resultados = []

    for month in range(1, 13):
        data_busca = f"{month:02d}/{data_atual.strftime('%Y')}"
        total = df["data_prevista"].astype(str).str.contains(data_busca).sum()
        resultados.append({"Mes": f"{month:02d}", "Total": total})

    df_estatistica = pd.DataFrame(resultados)

    fig = px.bar(
        df_estatistica,
        x="Mes",
        y="Total",
        title=f"Estatística Mensal - {data_atual.strftime('%Y')}",
        labels={"Mes": "Mês", "Total": "Entradas"},
    )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=30, r=30, t=35, b=30),
    )
    return fig.to_html(full_html=False, include_plotlyjs=False)
