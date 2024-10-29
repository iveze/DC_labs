money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0

while True:
    money_capital += salary
    money_capital -= spend
    if (money_capital < 0):
        break
    spend *= (1 + increase)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
