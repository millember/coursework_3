from datetime import datetime
from dataclasses import dataclass


@dataclass
class Operation:
    id: int
    state: str
    date: str
    operationAmount: dict
    description: str
    to: str
    where: str = None

    @classmethod
    def from_dict(cls, array: list) -> list:
        """Returns list of class instances"""
        return [Operation(**x) for x in array]

    def edit_date(self, date: str) -> str:
        date = datetime.fromisoformat(self.date)
        date_operation = datetime.strftime(date, "%d.%m.%Y")
        return date_operation

    def hide_card_numbers(self, come_from: str) -> str:
        if come_from:
            account_info = "".join([x for x in self.where if not x.isnumeric()])
            card_nums = "".join([x for x in self.where if x.isnumeric()])
            return f"{account_info} {card_nums[:4]} {card_nums[6:8]}** **** {card_nums[-4:]}"

    def hide_account_numbers(self, to: str) -> str:
        """Returns string with hidden account numbers."""
        account_info = "".join([x for x in self.to if x.isalpha()])
        return f"{account_info} **{self.to[-4:]}"
