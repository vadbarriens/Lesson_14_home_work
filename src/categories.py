from src.products import Product


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

    def __str__(self):
        """
        Магический метод, возвращающий строковое отображение в необходимом виде
        """
        sum_products = 0
        for product in self.__products:
            sum_products += product.quantity
        return f'{self.name}, количество продуктов: {sum_products} шт.'

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")
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
                f"{str(product)}"
                for product in self.__products
            ]
        )
