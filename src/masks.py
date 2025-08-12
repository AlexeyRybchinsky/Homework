# src/masks.py


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX
    """
    clean = card_number.replace(" ", "")
    if len(clean) != 16 or not clean.isdigit():
        raise ValueError("Invalid card number")
    return f"{clean[:4]} {clean[4:6]}** **** {clean[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета в формате **XXXX
    """
    clean = account_number.replace(" ", "")
    if len(clean) < 4 or not clean.isdigit():
        raise ValueError("Invalid account number")
    return f"**{clean[-4:]}"
