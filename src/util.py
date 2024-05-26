import json
from pathlib import Path


def operation_json() -> list:
    path = Path("../data_operation/operations.json")
    with path.open("r", encoding="utf-8") as file:
        content = file.read()
        data = json.loads(content)
    return data


def from_operations(data: list) -> list:
    """Returns edited list of operations."""
    list_from = [x for x in data if x.get("from")]
    for x in list_from:
        x['where'] = x.pop('from')
    return list_from


def sort_operations(data: list) -> list:
    """Returns sorted list of operations by data."""
    list_from = [x for x in data if x.get("date")]
    list_sorted = sorted(list_from, key=lambda x: x["date"], reverse=True)
    return list_sorted
