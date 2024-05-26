import pytest
from src.operation import Operation


@pytest.fixture
def example_data():
    return Operation(
        id=441945886,
        state="EXECUTED",
        date="019-08-26T10:50:58.294041",
        operationAmount={
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        description="Перевод организации",
        where="Maestro 1596837868705199",
        to="Счет 64686473678894779589",
    )


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
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "where": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
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
        Operation(
            id=939719570,
            state="EXECUTED",
            date="2018-06-30T02:08:58.425572",
            operationAmount={
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 11776614605963066702",
            where="Счет 75106830613657916952",
        ),
    ]


def test_field_access(example_data):
    operation = example_data
    assert operation.id == 441945886
    assert operation.state == "EXECUTED"
    assert operation.date == "019-08-26T10:50:58.294041"
    assert operation.operationAmount == {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    }
    assert operation.description == "Перевод организации"
    assert operation.where == "Maestro 1596837868705199"
    assert operation.to == "Счет 64686473678894779589"


def test_from_list(list_of_examples, list_of_operations):
    assert Operation.from_dict(list_of_examples) == list_of_operations


def test_equality(example_data):
    operation_1 = example_data
    operation_2 = example_data
    assert operation_1 == operation_2


def test_inequality(list_of_examples):
    operation_1 = Operation(**list_of_examples[0])
    operation_2 = Operation(**list_of_examples[1])
    assert operation_1 != operation_2


def test_identity(example_data):
    operation_1 = example_data
    operation_2 = example_data
    assert operation_1 is operation_2
