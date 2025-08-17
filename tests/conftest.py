from typing import Any, Dict, List

import pytest

Operation = Dict[str, Any]


@pytest.fixture()
def operations_sample() -> List[Operation]:
    # Базовый набор из условия
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()
def operations_equal_dates() -> List[Operation]:
    # Одинаковые даты для проверки стабильности сортировки
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


@pytest.fixture()
def operations_with_bad_date() -> List[Operation]:
    # Некорректная дата для негативных тестов сортировки
    return [
        {"id": 1, "state": "EXECUTED", "date": "not-a-date"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]
