import csv
from abc import ABC
from src.instantiate import InstantiateCSVError

class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return float(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        """
        Создаем исключения
        """
        try:
            with open("../src/items.csv", encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if "name" and "price" and "quantity" in row:
                        cls(row['name'], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(line):
        number = int(float(line))
        return number

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception