import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data, encode_bill_info


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x["date"] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-15T11:47:40.496961", "2018-10-14T08:21:33.419441"]


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['14.10.2018 Перевод с карты на счет \nMaestro 3928 54** **** 4026 -> Счет ** 3493 \n77751.04 руб.', '26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 -> Счет ** 9589 \n31957.58 руб.', '15.07.2019 Открытие вклада \nСчет ** 2265 \n92688.46 USD', '22.07.2018 Перевод организации \nСчет ** 4147 -> Счет ** 7473 \n92130.50 USD']


@pytest.mark.parametrize("test_input,expected", [
    ("Счет 90887717138446397473", "Счет ** 7473"),
    ("Visa Classic 2842878893689012", "Visa Classic 2842 87** **** 9012")
])
def test_encode_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected