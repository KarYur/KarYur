from geopy.geocoders import Nominatim
from haversine import haversine

def get_coordinates(address):
    """
    Возвращает координаты (широту и долготу) по введенному адресу.
    :param address: Адрес на русском языке.
    :return: Кортеж с координатами (широта, долгота).
    """
    geolocator = Nominatim(user_agent="delivery_calculator")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Не удалось найти координаты для адреса: {address}")

def calculate_delivery_cost(address, office_address="Перовское шоссе, 9с1, Москва, 109202"):
    """
    Рассчитывает стоимость доставки на основе введенного адреса.
    :param address: Адрес доставки.
    :param office_address: Адрес офиса отправления (по умолчанию Перовское шоссе, 9с1, Москва, 109202).
    :return: Стоимость доставки в рублях.
    """
    cost_moscow = 5000  # фиксированная цена доставки в Москве
    cost_per_km_moscow_region = 100  # цена за километр в Московской области

    # Получаем координаты офиса и точки доставки
    office_coords = get_coordinates(office_address)
    delivery_coords = get_coordinates(address)

    # Рассчитываем расстояние в километрах между офисом и точкой доставки
    distance = haversine(office_coords, delivery_coords)

    # Определяем, находится ли адрес в пределах Москвы
    if "Москва" in address:
        return cost_moscow
    else:
        return cost_per_km_moscow_region * distance

# Пример использования
address = input("Введите адрес доставки: ")
try:
    cost = calculate_delivery_cost(address)
    print(f"Стоимость доставки: {cost} рублей")
except ValueError as e:
    print(e)
