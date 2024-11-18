const container_imagem = document.querySelectorAll(".image-feed");
const text = "Seu Feed Está Aqui!"; // Texto a ser exibido
const typingElement = document.getElementById("typing-effect");
let index = 0;

window.addEventListener('load', () => { // Quando a página carregar
  requestAnimationFrame(() => {
    container_imagem.forEach((imagem) => {
      imagem.style.scale="1"; // Altera a escala com transição
    });
  });
});

function typeEffect() {
  if (index < text.length) {
    typingElement.textContent += text.charAt(index); // Adiciona o próximo caractere
    index++;
    setTimeout(typeEffect, 50); // Intervalo entre cada caractere
  }
}

typeEffect();