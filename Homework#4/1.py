
from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - input_date
        return difference.days
    except:
        print("помилка, невірний формат дати")
        return None

input_from_user = input("Введіть дату у форматі YYYY-MM-DD: ")

days_diff = get_days_from_today(input_from_user)

if days_diff is not None:
    print(f"Різниця між введеною та сьогоднішньою датою: {days_diff} днів")

