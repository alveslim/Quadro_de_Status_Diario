document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide-item');
    if (slides.length === 0) return;

    let currentIndex = 0;
    const tempoTroca = 15000;

    // VERIFICAÇÃO CRÍTICA: Se existir o slide com a classe de alerta
    const slideHoje = document.getElementById('slide-hoje');
    const temCritico = slideHoje && slideHoje.classList.contains('tem-item-critico');

    if (temCritico) {
        // Redireciona a tela IMEDIATAMENTE para o slide de Hoje
        slides.forEach(slide => slide.classList.remove('active', 'exit'));
        slideHoje.classList.add('active');

        // Atualiza o índice do slider para o slide de hoje (índice 0)
        currentIndex = 0;

        console.warn("⚠️ ALERTA CRÍTICO ENCONTRADO! Tela redirecionada para HOJE.");
    }

    const trocarSlide = () => {
        const slideAtual = slides[currentIndex];

        slideAtual.classList.remove('active');
        slideAtual.classList.add('exit');

        setTimeout(() => {
            slideAtual.classList.remove('exit');
        }, 800);

        currentIndex = (currentIndex + 1) % slides.length;
        const proximoSlide = slides[currentIndex];

        proximoSlide.classList.add('active');

        const plotlyGraphs = proximoSlide.querySelectorAll('.js-plotly-plot');
        plotlyGraphs.forEach(graph => {
            if (window.Plotly) {
                window.Plotly.Plots.resize(graph);
            }
        });
    };

    setInterval(trocarSlide, tempoTroca);
});
