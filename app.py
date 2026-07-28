from datetime import date
import pandas as pd

data_atual = date.today()
# print(data_atual)
data_br = data_atual.strftime("%d/%m/%Y")
# print(data_br)
data = "27/07/2026"
df = pd.read_csv("dado.csv")
resultado = df[df["data_prevista"] == "27/07/2026"]
if not resultado.empty:
    # Índice da linha no DataFrame (0-indexed)
    linha_df = resultado.index[0]
    nome_coluna = "status"

    # Salva a posição/referência na variável
    posicao = {"linha_index": linha_df, "coluna": nome_coluna}

    # Acessa o valor nessa posição exata
    valor_exato = df.at[linha_df, nome_coluna]
    print(
        f"Posição no DF: linha {linha_df}, coluna '{nome_coluna}' -> Valor: {valor_exato}"
    )
