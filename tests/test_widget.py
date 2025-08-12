from src.widget import get_date, mask_account_card


def test_mask_account_card_card() -> None:
    assert (
        mask_account_card("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )


def test_mask_account_card_account() -> None:
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_get_date_basic() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_with_z() -> None:
    assert get_date("2018-07-11T02:26:18Z") == "11.07.2018"
