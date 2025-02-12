from src.products import Product


def test_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_price_getter_setter():
    """
    Проверка геттера и сеттера цены.
    """
    product = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )

    # Проверяем геттер
    assert product.price == 120000.50

    # Пытаемся установить некорректную цену
    product.price = -100
    assert product.price == 120000.50  # Цена не изменилась

    # Устанавливаем корректную цену
    product.price = 130000.00
    assert product.price == 130000.00


def test_products_str(first_product):
    """Проверка корректного вывода строки класса продукты"""
    assert (
        str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_products_add(first_product, second_product):
    """Проверка сложения сумм цен товаров"""
    assert first_product + second_product == 2580000.0
