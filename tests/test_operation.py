import pytest
from src.operation import Operation


@pytest.fixture
def list_of_examples():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "where": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "where": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


@pytest.fixture()
def list_of_operations():
    return [
        Operation(
            id=441945886,
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            operationAmount={
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод организации",
            to="Счет 64686473678894779589",
            where="Maestro 1596837868705199",
        ),
        Operation(
            id=41428829,
            state="EXECUTED",
            date="2019-07-03T18:35:29.512364",
            operationAmount={
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 35383033474447895560",
            where="MasterCard 7158300734726758",
        ),
    ]


def test_from_list(list_of_examples, list_of_operations):
    assert Operation.from_dict(list_of_examples) == list_of_operations


def test_inequality(list_of_examples):
    assert Operation(**list_of_examples[0]) != Operation(**list_of_examples[1])


def test_date(list_of_examples):
    operation = Operation.from_dict(list_of_examples)
    date_operation = operation[0]
    assert date_operation.edit_date(date_operation.date) == "26.08.2019"


def test_card(list_of_examples):
    operation = Operation.from_dict(list_of_examples)
    date_operation = operation[0]
    assert date_operation.hide_card_numbers(date_operation.where) == "Maestro 1596 83** **** 5199"


def test_account(list_of_examples):
    operation = Operation.from_dict(list_of_examples)
    date_operation = operation[0]
    assert date_operation.hide_account_numbers(date_operation.to) == "Счет **9589"
