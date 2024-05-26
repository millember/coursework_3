from src.main import main, output
from src.operation import Operation


def test_main():
    assert main() == [
        Operation(
            id=114832369,
            state="EXECUTED",
            date="2019-12-07T06:17:14.634890",
            operationAmount={
                "amount": "48150.39",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 35158586384610753655",
            where="Visa Classic 2842878893689012",
        ),
        Operation(
            id=154927927,
            state="EXECUTED",
            date="2019-11-19T09:22:25.899614",
            operationAmount={
                "amount": "30153.72",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод организации",
            to="Счет 43241152692663622869",
            where="Maestro 7810846596785568",
        ),
        Operation(
            id=482520625,
            state="EXECUTED",
            date="2019-11-13T17:38:04.800051",
            operationAmount={
                "amount": "62814.53",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод со счета на счет",
            to="Счет 46765464282437878125",
            where="Счет 38611439522855669794",
        ),
        Operation(
            id=509645757,
            state="EXECUTED",
            date="2019-10-30T01:49:52.939296",
            operationAmount={
                "amount": "23036.03",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод с карты на счет",
            to="Счет 48943806953649539453",
            where="Visa Gold 7756673469642839",
        ),
        Operation(
            id=888407131,
            state="EXECUTED",
            date="2019-09-29T14:25:28.588059",
            operationAmount={
                "amount": "45849.53",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод со счета на счет",
            to="Счет 46723050671868944961",
            where="Счет 35421428450077339637",
        ),
    ]


def test_output():
    assert output(
        main(1)) == ['07.12.2019 Перевод организации \nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n']
