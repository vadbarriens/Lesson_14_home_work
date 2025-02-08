from src.categories import Category


def test_category_init(categories):
    assert categories.name == "Телевизоры"
    assert categories.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert categories.products == "product1"
    assert Category.category_count == 1
    assert Category.product_count == 8
