import pytest

from src.categories import Category
from src.products import Product


def test_category_init(categories):
    """
    Проверка инициализации класса
    """
    assert categories.name == "Телевизоры"
    assert categories.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert Category.category_count == 1
    assert Category.product_count == 8


def test_add_product():
    """
    Проверка добавления товара в категорию.
    """
    # Создаем категорию
    category = Category(
        name="Электроника", description="Техника для дома и офиса", products=[]
    )

    # Создаем товар
    product = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )

    # Добавляем товар в категорию
    category.add_product(product)

    # Проверяем, что товар добавлен
    assert Category.product_count == 9
    assert category.get_products()[0].name == "Ноутбук"


def test_get_products():
    """
    Проверка получения списка товаров.
    """
    product1 = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )
    product2 = Product(
        name="Смартфон",
        description="Смартфон с OLED-экраном",
        price=80000.00,
        quantity=25,
    )
    category = Category(
        name="Электроника",
        description="Техника для дома и офиса",
        products=[product1, product2],
    )

    products = category.get_products()
    assert len(products) == 2
    assert products[0].name == "Ноутбук"
    assert products[1].name == "Смартфон"


def test_category_products_getter():
    """
    Проверка геттера для получения списка товаров в виде строки.
    """
    product1 = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )
    product2 = Product(
        name="Смартфон",
        description="Смартфон с OLED-экраном",
        price=80000.00,
        quantity=25,
    )
    category = Category(
        name="Электроника", description="Техника для дома и офиса", products=[]
    )

    category.add_product(product1)
    category.add_product(product2)

    # Проверяем вывод списка товаров
    expected_output = (
        "Ноутбук, 120000.5 руб. Остаток: 10 шт.\nСмартфон, 80000.0 руб. Остаток: 25 шт."
    )
    assert category.products == expected_output


def test_add_product1():
    """
    Проверка добавления товара в категорию.
    """
    # Создаем категорию
    category = Category(
        name="Электроника", description="Техника для дома и офиса", products=[]
    )

    # Создаем товар
    product = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )

    # Добавляем товар в категорию
    category.add_product(product)

    # Проверяем, что товар добавлен
    assert len(category.get_products()) == 1
    assert category.get_products()[0].name == "Ноутбук"
    assert Category.product_count == 14  # Общее количество товаров увеличилось


def test_categories_str(categories1):
    """Проверка корректного вывода строки класса категории"""
    assert str(categories1) == "Электроника, количество продуктов: 10 шт."


def test_add_product_error(smartphone1):
    category_smartphones = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [
            smartphone1,
        ],
    )
    with pytest.raises(TypeError):
        category_smartphones.add_product()
