from src.operation import Operation
from src import util


def main(number=5):
    list_operations = util.operation_json("../data_operation/operations.json")
    operations_edited = util.from_operations(list_operations)
    sorted_operations = util.sort_operations(operations_edited)
    last_operations = util.last_operation(sorted_operations, number)
    operations = Operation.from_dict(last_operations)
    return [x for x in operations]


def output(name):
    transactions = name
    out_text = list()
    for operation in transactions:
        out_text.append(
            f"{operation.edit_date(operation.date)} {operation.description} \n"
            f"{operation.hide_card_numbers(operation.where)} -> {operation.hide_account_numbers(operation.to)}\n"
            f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n"
        )
    return out_text


if __name__ == "__main__":
    out = output(main(1))
    print('\n'.join(out))
