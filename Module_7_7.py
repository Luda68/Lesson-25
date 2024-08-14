# %
team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_num = 5
team2_num = 6
print("В команде %(team1)s участников: %(team1_num)s!" % {"team1": "Мастера кода", "team1_num": 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {"team1_num": 5, "team2_num": 6})

#format()
score_2 = 42          # количество задач решённых командой 2
team1_time = 18015.2  # время за которое команда 2 решила задачи
print("Команда Волшебники данных решила задач: {}!". format(score_2))
print("Волшебники данных решили задачи за {}!". format(team1_time))

#f-строка
score_1 = 40       #количество решённых задач по командам
score_2 = 42
print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = "Результат битвы"
print(f"{challenge_result}: победа команды {team1}!")

tasks_total = 82
time_avg = "350,4 c на задачу"
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg}!")


