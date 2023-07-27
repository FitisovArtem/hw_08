from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    result = {}
    if len(users) < 1:   #Проверка на пустоту списка сотрудников
        return f"Список сотрудников пуст"
    dt_now = datetime.now()
    for employee in users:
        bd = datetime.strptime(employee.get("birthday"), "%Y-%m-%d") #Преобразование полученно даты
        bd_date = datetime(year=bd.year, month=bd.month, day=bd.day)
        difference = bd_date - datetime(year=dt_now.year, month=dt_now.month, day=dt_now.day) #Получаем разницы между текущей датой и датой рождения сотрудника
        if difference.days >= 0 and difference.days < 7: # Проверяем что дата рождения сотрудника выпадает на ближ 7 дней
            if bd_date.weekday() == 5:    #Если ДР в субботу  - 
                bd_date = bd_date + timedelta(days=2)   # Переносим на понедельник
            if bd_date.weekday() == 6:    #Если ДР в воскресенье  - 
                bd_date = bd_date + timedelta(days=1)   # Переносим на понедельник
            if bd_date.strftime('%A') not in result:    # Собираем в словарь для объединения по дням недели
                result[bd_date.strftime('%A')] = []
            result[bd_date.strftime('%A')].append(employee.get('name'))
    
    for key,value in result.items():       # перебираем словарь для вывода имен сотрудников по дням недели 
	    print(key, ': ', ", ".join(value))              





users = [{"name": "Ann R","birthday": "2022-07-26"},
         {"name": "Li Re","birthday": "2023-07-27"},
         {"name": "Maf RT","birthday": "2023-07-28"},
         {"name": "TRE gh","birthday": "2023-07-29"},
         {"name": "firere","birthday": "2023-07-30"},
         {"name": "elkrel","birthday": "2023-06-06"},
         {"name": "qqqqqq","birthday": "2023-08-01"},
         {"name": "ttttttt","birthday": "2023-08-01"}]

print(get_birthdays_per_week(users))

