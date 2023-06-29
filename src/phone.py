from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__name = name
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def name(self):
        return self.__name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__number_of_sim = number


from src.item import Item


class MixinLog:

    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class Keyboard(Item, MixinLog):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)