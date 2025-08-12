from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(raw: str) -> str:
    """
    Возвращаем строку с замаскированным номером карты/счёта.
    """
    text = raw.strip()
    if not text:
        raise ValueError("Пустая строка.")

    parts = text.split()
    number = parts[-1] if parts else ""
    name = " ".join(parts[:-1]) if len(parts) > 1 else ""

    if not number.isdigit():
        raise ValueError("Ожидался числовой идентификатор в конце строки.")

    if name.startswith("Счет"):
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}".strip()


def get_date(iso_dt: str) -> str:
    """
    Преобразуем дату в формат 'ДД.ММ.ГГГГ'.
    """
    fixed = iso_dt.replace("Z", "+00:00")
    dt = datetime.fromisoformat(fixed)
    return dt.strftime("%d.%m.%Y")
