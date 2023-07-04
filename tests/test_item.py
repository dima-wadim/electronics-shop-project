"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone
from src.instantiate import InstantiateCSVError


@pytest.fixture()
def item_name():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_name):
    assert item_name.price == 10000
    assert item_name.name == "Смартфон"
    assert item_name.quantity == 20


def test_item_calculation(item_name):
    assert item_name.calculate_total_price() == 200000.0


def test_item_discount(item_name):
    item_name.pay_rate = 0.8
    item_name.apply_discount()
    assert item_name.price == 8000.0


def test_get_name(item_name):
    assert item_name.name == "Смартфон"


def test_set_name(item_name):
    item_name.name = "СуперСмартфон"
    assert item_name.name == "СуперСмарт"
    item_name.name = "ХуавейНова"
    assert item_name.name == "ХуавейНова"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item_name1 = Item.all[0]
    assert item_name1.name == "Смартфон"
    item_name2 = Item.all[1]
    assert item_name2.name == "Ноутбук"


def test_string_to_number():
    Item.instantiate_from_csv()
    assert Item.string_to_number("5.3") == 5


def test_str(item_name):
    assert str(item_name) == "Смартфон"


def test_repr(item_name):
    assert repr(item_name) == "Item('Смартфон', 10000, 20)"


def test_add(item_name):
    phone2 = Phone("iPhone 14", 100000, 10, 3)
    assert item_name + phone2 == 30
    assert item_name + item_name == 40

def test_instantiate_from_csv_inst_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()