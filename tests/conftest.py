import pytest


@pytest.fixture
def test_data():
    return [
        {"date": "2018-10-14T08:21:33.419441",
         "description": "Перевод с карты на счет",
         "from": "Maestro 3928549031574026",
         "id": 615064591,
         "operationAmount": { "amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
         "state": "CANCELED",
         "to": "Счет 84163357546688983493"},
        {"date": "2019-08-26T10:50:58.294041",
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
         "to": "Счет 64686473678894779589"},
        {"date": "2019-07-15T11:47:40.496961",
         "description": "Открытие вклада",
         "id": 207126257,
         "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 35737585785074382265"},
        {"date": "2018-07-22T07:42:32.953324",
         "description": "Перевод организации",
         "from": "Счет 19628854383215954147",
         "id": 879660146,
         "operationAmount": {"amount": "92130.50", "currency": {"name": "USD", "code": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 90887717138446397473"}]