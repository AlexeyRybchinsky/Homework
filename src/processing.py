from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, в котором только те элементы,
    у которых значение ключа 'state' совпадает с переданным.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, отсортированный по ключу 'date'.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)
