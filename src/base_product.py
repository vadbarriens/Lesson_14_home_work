from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        """
        Абстрактный метод класса Product
        """
        pass
