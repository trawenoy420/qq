profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
cash = profit - costs
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {cash / profit:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")