import pytest

from src.widget import get_date, mask_account_card

# def test_mask_account_card_card() -> None:
#     assert (
#         mask_account_card("Visa Platinum 7000792289606361")
#         == "Visa Platinum 7000 79** **** 6361"
#     )
#
#
# def test_mask_account_card_account() -> None:
#     assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
#
#
# def test_get_date_basic() -> None:
#     assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
#
#
# def test_get_date_with_z() -> None:
#     assert get_date("2018-07-11T02:26:18Z") == "11.07.2018"


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card_for_cards(raw: str, expected: str) -> None:
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_for_accounts(raw: str, expected: str) -> None:
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "",
        "Visa Platinum notanumber",
        "Счет 123",
    ],
)
def test_mask_account_card_invalid(raw: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(raw)


@pytest.mark.parametrize(
    "iso, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18Z", "11.07.2018"),
        ("2020-12-31T23:59:59+03:00", "31.12.2020"),
        ("2024-03-11", "11.03.2024"),
    ],
)
def test_get_date_ok(iso: str, expected: str) -> None:
    assert get_date(iso) == expected


@pytest.mark.parametrize("bad", ["not-a-date", "2024/03/11", ""])
def test_get_date_invalid(bad: str) -> None:
    with pytest.raises(ValueError):
        get_date(bad)
