import pytest

from src.masks import get_mask_account, get_mask_card_number


# def test_get_mask_card_number() -> None:
#     assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
#
#
# def test_get_mask_account() -> None:
#     assert get_mask_account("73654108430135874305") == "**4305"

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number_ok(raw: str, expected: str) -> None:
    assert get_mask_card_number(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "",
        "1234",
        "7000-7922-8960-6361",
        "abcdefabcdefabcd",
    ],
)
def test_get_mask_card_number_invalid(raw: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(raw)


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("73654108430135874305", "**4305"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("0000", "**0000"),
    ],
)
def test_get_mask_account_ok(raw: str, expected: str) -> None:
    assert get_mask_account(raw) == expected


@pytest.mark.parametrize("raw", ["", "123", "12 3", "abcd"])
def test_get_mask_account_invalid(raw: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(raw)