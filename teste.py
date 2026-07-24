import os
from flask import Flask, jsonify, render_template_string
import pandas as pd

app = Flask(__name__)
ARQUIVO_EXCEL = "dados.xlsx"


def criar_excel_exemplo():
    """Cria um arquivo Excel fictício caso ele ainda não exista."""
    if not os.path.exists(ARQUIVO_EXCEL):
        dados = {
            "Indicador": [
                "Vendas de Hoje",
                "Meta Mensal (%)",
                "Usuários Ativos",
                "Status do Sistema",
            ],
            "Valor": ["R$ 14.530", "85%", "1.240", "Online 🟢"],
        }
        df = pd.DataFrame(dados)
        df.to_excel(ARQUIVO_EXCEL, index=False)
        print(f"Arquivo '{ARQUIVO_EXCEL}' gerado com sucesso para teste!")


# HTML do Painel (Otimizado para telas de TV)
HTML_PAINEL = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel TV - Ao Vivo</title>
    <style>
        body {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 90vh;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            color: #38bdf8;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .status-bar {
            font-size: 1.2rem;
            color: #94a3b8;
            margin-bottom: 50px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            width: 100%;
            max-width: 1400px;
        }
        .card {
            background-color: #1e293b;
            border: 2px solid #334155;
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            transition: transform 0.2s;
        }
        .card-title {
            font-size: 1.8rem;
            color: #94a3b8;
            margin-bottom: 20px;
        }
        .card-value {
            font-size: 4rem;
            font-weight: bold;
            color: #38bdf8;
        }
    </style>
</head>
<body>

    <h1>Painel de Operações</h1>
    <div class="status-bar">Atualização automática via Excel • <span id="relogio"></span></div>

    <div class="grid" id="grid-cards">
        <!-- Os dados do Excel serão injetados aqui pelo JavaScript -->
    </div>

    <script>
        function atualizarRelogio() {
            const agora = new Date();
            document.getElementById('relogio').innerText = agora.toLocaleTimeString('pt-BR');
        }

        async function buscarDados() {
            try {
                const resposta = await fetch('/api/dados');
                const dados = await resposta.json();
                
                const grid = document.getElementById('grid-cards');
                grid.innerHTML = ''; // Limpa os cards antigos

                dados.forEach(item => {
                    const card = document.createElement('div');
                    card.className = 'card';
                    card.innerHTML = `
                        <div class="card-title">${item.Indicador}</div>
                        <div class="card-value">${item.Valor}</div>
                    `;
                    grid.appendChild(card);
                });
            } catch (erro) {
                console.error("Erro ao buscar dados do Excel:", erro);
            }
        }

        // Atualiza o relógio a cada segundo
        setInterval(atualizarRelogio, 1000);
        atualizarRelogio();

        // Busca os dados do Excel a cada 3 segundos
        buscarDados();
        setInterval(buscarDados, 3000);
    </script>
</body>
</html>
"""


@app.route("/")
def painel():
    return render_template_string(HTML_PAINEL)


@app.route("/api/dados")
def api_dados():
    """Lê o Excel em tempo real e envia como JSON para o painel."""
    try:
        df = pd.read_excel(ARQUIVO_EXCEL)
        # Converte o DataFrame para uma lista de dicionários
        dados_json = df.to_dict(orient="records")
        return jsonify(dados_json)
    except Exception as e:
        return jsonify([{"Indicador": "Erro na Leitura", "Valor": str(e)}]), 500


if __name__ == "__main__":
    criar_excel_exemplo()
    print("\n--- SERVIDOR INICIADO ---")
    print("Para ver no seu PC, acesse: http://localhost:5000")
    print("Para ver na TV, descubra o IP do PC e acesse na TV: http://SEU_IP:5000")
    print("-------------------------\n")
    # 0.0.0.0 permite que a TV (na mesma rede Wi-Fi) acesse o computador
    app.run(host="0.0.0.0", port=5000, debug=True)