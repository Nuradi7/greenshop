const counterNode = document.querySelector('.product-view__counter');
const incBtnNode = document.querySelector('.js-inc-btn')
const clearBtnNode = document.querySelector('.js-clear-btn')

let counter = 0;

function increment() {
    counter += 1;
}

function clear() {
    counter -= 1;
}

function render() {
    counterNode.innerText = counter;
}

incBtnNode.addEventListener('click', () => {
    increment();
    render();
});

clearBtnNode.addEventListener('click', () => {
    clear();
    render();
});

render();

const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
});

function viewDiv(){
    document.getElementById("row").style.display = "block";
    document.getElementById("description__wrapper").style.display = "none";
  };

function openDiv(){
    document.getElementById("description__wrapper").style.display = "block";
    document.getElementById("row").style.display = "none";
  };

