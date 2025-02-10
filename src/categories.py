from src.products import Product

class Category:
    """Класс, подсчитывающий количество товаров и количество категорий"""

    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self):
        list_product = ''
        for prod in self.__products:
            list_product = f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.'
        return list_product
