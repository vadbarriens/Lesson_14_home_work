class Product:
    """Класс, описывающий товары, цену и наличие"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_price < self.__price:
                user_response = input('цена товара понижается, если согласны нажмите "y" (yes): ')
                if user_response == 'y':
                    self.__price = new_price

    @classmethod
    def new_product(cls, dict_products):
        name = dict_products['name']
        description = dict_products['description']
        quantity = dict_products['quantity']
        price = dict_products['price']
        return cls(name, description, price, quantity)



