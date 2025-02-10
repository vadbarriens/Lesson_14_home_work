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
        for product in self.__products:
            list_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return list_product
