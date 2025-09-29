let DISC = {
    '1': 'Иллюстрация влюблённые мышки на льду была придумана как рождественская картинка для детей',
    '2': 'Рисунок ночи символизирует гармонию между быстротечностью времени и безграничным спокойствием',
};
let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";

let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");

btn1.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести информацию по мышкам");
        item = "1"; // ID для "мышек"
        tg.MainButton.show();
    }
});

btn2.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести информацию по ночи");
        item = "2"; // ID для "ночи"
        tg.MainButton.show();
    }
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});
