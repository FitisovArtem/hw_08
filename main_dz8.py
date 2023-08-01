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
        
        if (difference.days >= 0 and difference.days < 7 and dt_now.weekday() > 0) or (difference.days >= -2 and difference.days < 5 and dt_now.weekday() == 0): # Проверяем что дата рождения сотрудника выпадает на ближ 7 дней + проверка на понедельник (с учетом др выпавших на прошедшие выходные)
            if bd_date.weekday() == 5:    #Проверка что ДР был в субботу
                bd_date = bd_date + timedelta(days=2)   # Переносим на понедельник др за прошедшую субботу
            if bd_date.weekday() == 6:    #Проверка что ДР был в воскресенье
                bd_date = bd_date + timedelta(days=1)   # Переносим на понедельник др за прошедшее воскресенье
            if bd_date.strftime('%A') not in result:    # Проверяем наличие дня с днями рождения сотрудников в словаре
                result[bd_date.strftime('%A')] = []     # Собираем в словарь для объединения по дням недели
            result[bd_date.strftime('%A')].append(employee.get('name'))   # Добавляем в словарь сотрудника в необзодимы день недели
   
    for key,value in result.items():       # перебираем словарь для вывода имен сотрудников по дням недели 
	    print(key, ': ', ", ".join(value))              





users = [{"name": "qqqqqq","birthday": "2023-07-02"},
        {"name": "Ann R","birthday": "2023-07-28"},
         {"name": "Li Re","birthday": "2023-07-29"},
         {"name": "Maf RT","birthday": "2023-07-30"},
         {"name": "TRE gh","birthday": "2023-07-31"},
         {"name": "firere","birthday": "2023-08-01"},
         {"name": "wwwwwww","birthday": "2023-08-04"},
         {"name": "elkrel","birthday": "2023-08-05"},
         {"name": "ttttttt","birthday": "2023-08-06"},
         {"name": "ееееееее","birthday": "2023-08-07"}]

print(get_birthdays_per_week(users))

