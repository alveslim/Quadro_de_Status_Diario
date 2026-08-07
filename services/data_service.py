from datetime import date, timedelta
import pandas as pd
import pathlib
import plotly.express as px

DATA_PATH = r"\\192.168.1.15\dados\dado.csv"


def carregar_dados():
    try:
        # Usa pathlib para lidar de forma robusta com caminhos de rede (UNC)
        path = pathlib.Path(DATA_PATH)

        df = pd.read_csv(path, dtype=str, keep_default_na=False)
        df.columns = df.columns.str.strip()

        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()

        return df

    except (FileNotFoundError, PermissionError, OSError) as e:
        # Captura erros de arquivo não encontrado, falta de permissão ou queda de rede
        print(f"Erro ao acessar o arquivo na rede: {e}")
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

    # Filtra as linhas por data
    df_hoje = (
        df[df["DATA_PREVISTA"] == data_br].copy()
        if "DATA_PREVISTA" in df.columns
        else pd.DataFrame()
    )
    df_amanha = (
        df[df["DATA_PREVISTA"] == data_br_amanha].copy()
        if "DATA_PREVISTA" in df.columns
        else pd.DataFrame()
    )

    # REGRA: Considera crítico se a coluna CRITICO tiver algum valor marcado como critico/sim
    if "CRITICO" in df_hoje.columns:
        df_hoje["IS_CRITICO"] = (
            df_hoje["CRITICO"].str.upper().isin(["CRITICO", "CRÍTICO", "SIM", "S", "1"])
        )
    else:
        df_hoje["IS_CRITICO"] = False

    tem_critico = df_hoje["IS_CRITICO"].any()

    return {
        "hoje": df_hoje.to_dict(orient="records"),
        "amanha": df_amanha.to_dict(orient="records"),
        "data_hoje": data_br,
        "data_amanha": data_br_amanha,
        "tem_critico": tem_critico,
    }


def gerar_grafico_pizza_html():
    df = carregar_dados()
    if df.empty or "CLIENTE" not in df.columns:
        return ""

    fig = px.pie(df, names="CLIENTE", title="Distribuição por Cliente")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=35, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


def gerar_grafico_mensal_html():
    df = carregar_dados()
    if df.empty or "DATA_PREVISTA" not in df.columns:
        return ""

    data_atual = date.today()
    resultados = []

    for month in range(1, 13):
        data_busca = f"{month:02d}/{data_atual.strftime('%Y')}"
        total = df["DATA_PREVISTA"].astype(str).str.contains(data_busca).sum()
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
