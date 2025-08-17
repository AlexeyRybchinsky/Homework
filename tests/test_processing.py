from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date

Operation = Dict[str, Any]


def test_filter_by_state_default(operations_sample: List[Operation]) -> None:
    result = filter_by_state(operations_sample)
    assert all(item["state"] == "EXECUTED" for item in result)
    assert [i["id"] for i in result] == [41428829, 939719570]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state_param(
    operations_sample: List[Operation], state: str, expected_ids: List[int]
) -> None:
    result = filter_by_state(operations_sample, state=state)
    assert [i["id"] for i in result] == expected_ids


def test_sort_by_date_desc(operations_sample: List[Operation]) -> None:
    result = sort_by_date(operations_sample)
    assert [i["id"] for i in result] == [41428829, 615064591, 594226727, 939719570]


def test_sort_by_date_asc(operations_sample: List[Operation]) -> None:
    result = sort_by_date(operations_sample, descending=False)
    assert [i["id"] for i in result] == [939719570, 594226727, 615064591, 41428829]


def test_sort_by_date_equal(operations_equal_dates: List[Operation]) -> None:
    result = sort_by_date(operations_equal_dates)
    assert len(result) == 3
    assert {i["id"] for i in result} == {1, 2, 3}


def test_sort_by_date_bad_input(operations_with_bad_date: List[Operation]) -> None:
    with pytest.raises(ValueError):
        sort_by_date(operations_with_bad_date)
