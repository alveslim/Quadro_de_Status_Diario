from flask import Flask, render_template
from services.data_service import (
    obter_dados_dashboard,
    gerar_grafico_pizza_html,
    gerar_grafico_mensal_html,
)

app = Flask(__name__)


# DESABILITA CACHE: Garante que o navegador receba os dados novos do CSV a cada requisição
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
    )
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response


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
