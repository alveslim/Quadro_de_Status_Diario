from flask import Flask, render_template
from services.data_service import (
    obter_dados_dashboard,
    gerar_grafico_pizza_html,
    gerar_grafico_mensal_html,
)

app = Flask(__name__)


@app.route("/")
def home():
    dados = obter_dados_dashboard()
    grafico_pizza = gerar_grafico_pizza_html()
    grafico_mensal = gerar_grafico_mensal_html()

    return render_template(
        "index.html",
        dados=dados,
        grafico_pizza=grafico_pizza,
        grafico_mensal=grafico_mensal,
    )


if __name__ == "__main__":
    print("Servidor Flask rodando em http://127.0.0.1:5000")
    app.run(debug=True)
