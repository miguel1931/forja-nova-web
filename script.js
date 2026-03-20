document.addEventListener('DOMContentLoaded', () => {
    console.log('FORJA NOVA: SISTEMA INICIALIZADO');

    // Efecto de parpadeo aleatorio en elementos con la clase .glitch-text
    const glitchTexts = document.querySelectorAll('.glitch-text');
    setInterval(() => {
        glitchTexts.forEach(text => {
            if (Math.random() > 0.95) {
                text.style.textShadow = `0 0 40px var(--doom-green)`;
                setTimeout(() => {
                    text.style.textShadow = `0 0 20px var(--doom-green-glow)`;
                }, 100);
            }
        });
    }, 500);

    // Simulación de "carga" en la terminal
    const values = document.querySelectorAll('.value');
    values.forEach(val => {
        const originalText = val.innerText;
        if (val.classList.contains('pulse')) return;
        
        val.innerText = '_';
        let i = 0;
        const typing = setInterval(() => {
            val.innerText = originalText.substring(0, i) + '_';
            i++;
            if (i > originalText.length) {
                val.innerText = originalText;
                clearInterval(typing);
            }
        }, 50 + Math.random() * 100);
    });
});
