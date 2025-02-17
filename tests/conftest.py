import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def categories():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products="product1",
    )


@pytest.fixture
def categories1():
    product1 = Product(
        name="Ноутбук",
        description="Мощный игровой ноутбук",
        price=120000.50,
        quantity=10,
    )
    category = Category(
        name="Электроника",
        description="Техника для дома и офиса",
        products=[product1],
    )
    return category
