from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, description, price, quantity):
        """
        Абстрактный метод класса Product
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
