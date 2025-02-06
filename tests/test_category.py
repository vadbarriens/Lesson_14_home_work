
def test_category_init(categories):
    assert categories.name == "Телевизоры"
    assert categories.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                      "станет вашим другом и помощником")
    assert categories.products == "product1"


def test_category_count(category_count):
    assert category_count == 1


def test_product_count(product_count):
    assert product_count == 2
