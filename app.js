document.getElementById('door-configurator').addEventListener('submit', function (e) {
    e.preventDefault();

    // Получение значений формы
    const width = parseFloat(document.getElementById('width').value);
    const height = parseFloat(document.getElementById('height').value);
    const material = document.getElementById('material').value;
    const system = document.getElementById('system').value;

    // Базовые цены за материалы и системы
    let pricePerSquareMeter = 0;
    let systemCost = 0;

    // Стоимость материалов
    if (material === 'glass') {
        pricePerSquareMeter = 4000;
    } else if (material === 'wood') {
        pricePerSquareMeter = 3000;
    } else if (material === 'metal') {
        pricePerSquareMeter = 5000;
    }

    // Стоимость системы
    if (system === 'sliding') {
        systemCost = 7000;
    } else if (system === 'folding') {
        systemCost = 10000;
    }

    // Рассчет общей стоимости
    const area = width * height;
    const totalPrice = (area * pricePerSquareMeter) + systemCost;

    // Отображение результата
    document.getElementById('result').innerText = `Примерная стоимость: ${totalPrice.toFixed(2)} руб.`;
});
