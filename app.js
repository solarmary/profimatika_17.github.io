// Initialize Telegram Web App
const tg = window.Telegram.WebApp;

tg.expand();
tg.MainButton.text = "Открыть";
tg.MainButton.show();

tg.onEvent('mainButtonClicked', () => {
    alert("Вы нажали кнопку!");
});

document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".grid-item");

    items.forEach(item => {
        item.addEventListener("click", () => {
            const pageUrl = item.getAttribute("href");
            tg.MainButton.setText("Открыть " + item.querySelector("p").textContent);
            tg.MainButton.show();
        });
    });
});
