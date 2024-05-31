import json
from pathlib import Path


def operation_json(road):
    path = Path(road)
    with path.open("r", encoding="utf-8") as file:
        content = file.read()
        data = json.loads(content)
    return data


def from_operations(data: list) -> list:
    list_from = [x for x in data if x.get("from")]
    for x in list_from:
        x['where'] = x.pop('from')
    return list_from


def sort_operations(data: list) -> list:
    list_from = [x for x in data if x.get("date")]
    list_sorted = sorted(list_from, key=lambda x: x["date"], reverse=True)
    return list_sorted


def last_operation(data: list, number: int) -> list:
    return [x for x in data[0: number + 1] if x["state"] == "EXECUTED"]
