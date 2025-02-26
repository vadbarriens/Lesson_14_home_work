from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс, описывающий товары, цену и наличие"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """
        Конструктор класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError ('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    def __str__(self):
        """
        Магический метод, возвращающий строковое отображение в необходимом виде
        :return:
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод, складывающий стоимости товаров с учётом количества на складе
        :param other:
        :return:
        """
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @property
    def price(self):
        """
        Геттер для получения цены товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Сеттер для установки цены товара.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_response = input(
                'цена товара понижается, если согласны нажмите "y" (yes): '
            )
            if user_response.lower() == "y":
                self.__price = new_price
            else:
                print("Изменение цены отклонено")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, dict_products, products=None):
        """
        Класс-метод для создания нового товара.
        """
        name = dict_products["name"]
        description = dict_products["description"]
        quantity = dict_products["quantity"]
        price = dict_products["price"]

        # Проверка на дубликаты
        if products:
            for product in products:
                if product.name == name:
                    # Обновляем количество и выбираем максимальную цену
                    product.quantity += quantity
                    product.__price = max(product.__price, price)
                    return product

        return cls(name, description, price, quantity)


class Smartphone(Product):
    """Подкласс смартфоны (расширенный от класса продукты)"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Подкласс смартфоны (расширенный от класса продукты)"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
