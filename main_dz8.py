from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    if len(users) < 1:
        return f"Список сотрудников пуст"
    dt_now = datetime.now()
    for employee in users:
        bd = datetime.strptime(employee.get("birthday"), "%Y-%m-%d")
        bd_date = datetime(year=bd.year, month=bd.month, day=bd.day)
        difference = bd_date - datetime(year=dt_now.year, month=dt_now.month, day=dt_now.day)
        if difference.days >= 0 and difference.days < 7:
            if bd_date.weekday() == 5:
                bd_date = bd_date + timedelta(days=2)
            if bd_date.weekday() == 6:
                bd_date = bd_date + timedelta(days=1)
            print(f"{bd_date.strftime('%A')}: {employee.get('name')}")
        



users = [{"name": "Ann R","birthday": "2023-07-26"},
         {"name": "Li Re","birthday": "2023-07-27"},
         {"name": "Maf RT","birthday": "2023-07-28"},
         {"name": "TRE gh","birthday": "2023-07-29"},
         {"name": "firere","birthday": "2023-07-30"},
         {"name": "elkrel","birthday": "2023-06-06"},
         {"name": "qqqqqq","birthday": "2023-08-01"}]

print(get_birthdays_per_week(users))

