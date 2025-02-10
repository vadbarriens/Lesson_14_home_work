class Category:
    """Класс, подсчитывающий количество товаров и количество категорий"""

    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """
        Конструктор класса Category
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """
        Добавляет товар в категорию.
        """
        self.__products.append(product)
        Category.product_count += 1

    def get_products(self):
        """
        Возвращает список товаров в категории.
        """
        return self.__products

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки.
        """
        return "\n".join(
            [
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                for product in self.__products
            ]
        )
