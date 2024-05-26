from src.operation import Operation
from src import util


def main():
    list_operations = util.operation_json()
    operations_edited = util.from_operations(list_operations)
    sorted_operations = util.sort_operations(operations_edited)
    last_operations = util.last_operation(sorted_operations, 5)
    operations = Operation.from_dict(last_operations)
    return [x for x in operations]


if __name__ == "__main__":
    transactions = main()
    for operation in transactions:
        print(
            f"{operation.edit_date(operation.date)} {operation.description} \n"
            f"{operation.hide_card_numbers(operation.where)} -> {operation.hide_account_numbers(operation.to)}\n"
            f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n"
        )
