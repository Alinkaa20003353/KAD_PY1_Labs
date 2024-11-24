salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Подушка безопасности за все месяцы

for month in range(months):
    deficit = spend - salary  # Дефицит за текущий месяц
    money_capital += deficit  # Суммируем дефицит
    spend *= (1 + increase)  # Увеличиваем расходы на 3%

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{money_capital:.2f}")
