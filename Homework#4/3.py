import re

def normalize_phone(phone_number: str) -> str:
    # 1. Видаляємо зайві пробіли на початку та в кінці
    phone_number = phone_number.strip()

    # 2. Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    # 3. Форматуємо номер відповідно до правил
    if phone_number.startswith("+"):
        # Якщо номер вже починається з '+', перевіримо чи є код країни
        if not phone_number.startswith("+38"):
            # Якщо міжнародний код не '+38', але починається з '380', додаємо '+'
            if phone_number.startswith("+380"):
                return phone_number
            else:
                # Залишаємо як є — або можна додати логіку для інших країн
                return phone_number
        else:
            return phone_number
    elif phone_number.startswith("380"):
        # Якщо номер починається з 380 — додаємо '+'
        return "+" + phone_number
    else:
        # Якщо номер без коду — додаємо '+38'
        return "+38" + phone_number


# 🔸 Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)