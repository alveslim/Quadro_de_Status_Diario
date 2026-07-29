from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML/CSS/JS integrado em uma única string para facilidade de execução rápida.
# Em um projeto Flask tradicional, este código ficaria dentro da pasta 'templates/index.html'.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slider de Texto Automático - Flask</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* Card Container Principal */
        .slider-card {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 16px;
            width: 90%;
            max-width: 650px;
            padding: 40px;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        .slider-header {
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #38bdf8;
            margin-bottom: 25px;
            font-weight: 600;
        }

        /* Container do Slider com overflow oculto para esconder o texto fora de cena */
        .slider-viewport {
            position: relative;
            height: 120px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Estilo base dos textos */
        .slide-item {
            position: absolute;
            width: 100%;
            font-size: 24px;
            font-weight: 500;
            line-height: 1.4;
            color: #f1f5f9;
            
            /* Posicionamento padrão inicial: fora da tela à direita e invisível */
            opacity: 0;
            transform: translateX(100%);
            transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.8s ease;
            pointer-events: none;
        }

        /* Estado ATIVO: Centralizado e visível */
        .slide-item.active {
            opacity: 1;
            transform: translateX(0%);
            pointer-events: auto;
        }

        /* Estado SAÍDA: Desliza para a esquerda e esconde */
        .slide-item.exit {
            opacity: 0;
            transform: translateX(-100%);
        }

        /* Barra de progresso visual (opcional) */
        .progress-bar-container {
            width: 100%;
            height: 4px;
            background-color: #334155;
            border-radius: 2px;
            margin-top: 30px;
            overflow: hidden;
        }

        .progress-bar-fill {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #38bdf8, #10b981);
            animation: progressLoop 4s linear infinite;
        }

        @keyframes progressLoop {
            0% { width: 0%; }
            100% { width: 100%; }
        }
    </style>
</head>
<body>

    <div class="slider-card">
        <div class="slider-header">⚡ Slider Automático Hands-Free</div>

        <!-- Área onde os textos deslizam -->
        <div class="slider-viewport">
            {% for msg in mensagens %}
                <div class="slide-item {% if loop.first %}active{% endif %}">
                    {{ msg }}
                </div>
            {% endfor %}
        </div>

        <!-- Indicador de progresso do tempo -->
        <div class="progress-bar-container">
            <div class="progress-bar-fill"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const slides = document.querySelectorAll('.slide-item');
            if (slides.length === 0) return;

            let currentIndex = 0;
            const tempoTroca = 4000; // Tempo em milissegundos (4 segundos)

            setInterval(() => {
                const slideAtual = slides[currentIndex];

                // 1. O slide atual desliza para a esquerda e sai
                slideAtual.classList.remove('active');
                slideAtual.classList.add('exit');

                // Limpa a classe de saída após a animação CSS terminar (0.8s)
                setTimeout(() => {
                    slideAtual.classList.remove('exit');
                }, 800);

                // 2. Calcula o índice do próximo slide (ciclo infinito)
                currentIndex = (currentIndex + 1) % slides.length;

                // 3. O próximo slide entra vindo da direita
                slides[currentIndex].classList.add('active');

            }, tempoTroca);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    # Mensagens enviadas dinamicamente pelo Flask
    mensagens_exemplo = [
        "👋 Bem-vindo ao nosso site em Flask!",
        "🚀 Este slider troca de texto 100% sozinho.",
        "✨ O texto desliza para o lado a cada 4 segundos.",
        "💻 Desenvolvido com CSS translateX e JavaScript."
    ]
    return render_template_string(HTML_TEMPLATE, mensagens=mensagens_exemplo)

if __name__ == '__main__':
    print("Servidor Flask rodando em http://127.0.0.1:5000")
    app.run(debug=True)