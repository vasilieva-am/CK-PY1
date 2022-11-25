money_capital = 20000  # Подушка безопасности
salary = 5000  # Зарплата
spend = 6000  # Затраты
increase = 0.05  # Рост цен

month = 0  # количество месяцев, на которые можно прожить

while True:
    delta = spend - salary
    if delta > money_capital:
        break

    month += 1
    money_capital -= delta
    spend *= 1 + increase

print(month)  # 8

