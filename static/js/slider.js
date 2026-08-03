document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide-item');
    if (slides.length === 0) return;

    let currentIndex = 0;
    const tempoTroca = 15000; // 15 segundos por slide
    let voltasCompletas = 0;

    // VERIFICAÇÃO CRÍTICA: Se existir item crítico no Slide de Hoje
    const slideHoje = document.getElementById('slide-hoje');
    const temCritico = slideHoje && slideHoje.classList.contains('tem-item-critico');

    if (temCritico) {
        slides.forEach(slide => slide.classList.remove('active', 'exit'));
        if (slideHoje) slideHoje.classList.add('active');
        currentIndex = 0;
        console.warn(" ALERTA CRÍTICO ENCONTRADO! Exibindo Slide de Hoje.");
    }

    const trocarSlide = () => {
        const slideAtual = slides[currentIndex];

        slideAtual.classList.remove('active');
        slideAtual.classList.add('exit');

        setTimeout(() => {
            slideAtual.classList.remove('exit');
        }, 800);

        // Avança o índice
        currentIndex = currentIndex + 1;

        // Se chegou ao fim do ciclo dos slides
        if (currentIndex >= slides.length) {
            currentIndex = 0;
            voltasCompletas++;

            // A cada 1 ciclo completo (ou após ver todos os slides), recarrega a página do servidor
            console.log("Ciclo completo finalizado. Recarregando dados do CSV...");
            window.location.reload();
            return;
        }

        const proximoSlide = slides[currentIndex];
        proximoSlide.classList.add('active');

        // Redimensiona gráficos Plotly caso existam no próximo slide
        const plotlyGraphs = proximoSlide.querySelectorAll('.js-plotly-plot');
        plotlyGraphs.forEach(graph => {
            if (window.Plotly) {
                window.Plotly.Plots.resize(graph);
            }
        });
    };

    setInterval(trocarSlide, tempoTroca);
});
