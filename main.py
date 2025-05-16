# Задание: Исследование оценок учеников
#
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить
# несколько шагов, чтобы проанализировать эти данные:

import pandas as pd
# 1. Самостоятельно создайте DataFrame с данными

grades = {
    "Math": [3, 4, 5, 3, 4, 4, 4, 5, 5, 5],
    "Chemistry": [3, 4, 5, 3, 4, 4, 4, 4, 4, 5],
    "Russian": [4, 5, 3, 5, 4, 5, 5, 4, 5, 3],
    "Literature": [3, 4, 3, 3, 5, 3, 4, 5, 4, 3],
    "English": [3, 3, 4, 5, 5, 4, 3, 4, 4, 4]
}

df = pd.DataFrame(grades)

# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно

print(df.head())

# 3. Вычислите среднюю оценку по каждому предмету

Math_mean = df["Math"].mean()
print(f'\nСредняя оценка по математике - {Math_mean}')
Chemistry_mean = df["Chemistry"].mean()
print(f'Средняя оценка по химии - {Chemistry_mean}')
Russian_mean = df["Russian"].mean()
print(f'Средняя оценка по русскому языку - {Russian_mean}')
Literature_mean = df["Literature"].mean()
print(f'Средняя оценка по литературе - {Literature_mean}')
English_mean = df["English"].mean()
print(f'Средняя оценка по английскому языку - {English_mean}')

# 4. Вычислите медианную оценку по каждому предмету

Math_median = df["Math"].median()
print(f'\nМедианная оценка по математике - {Math_median}')
Chemistry_median = df["Chemistry"].median()
print(f'Медианная оценка по химии - {Chemistry_median}')
Russian_median = df["Russian"].median()
print(f'Медианная оценка по русскому языку - {Russian_median}')
Literature_median = df["Literature"].median()
print(f'Медианная оценка по литературе - {Literature_median}')
English_median = df["English"].median()
print(f'Медианная оценка по английскому языку - {English_median}')

# 5. Вычислите Q1 и Q3 для оценок по математике:

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
print(f'\nQ1 и Q3 для оценок по математике - {Q1_math} и {Q3_math}')

# - можно также попробовать рассчитать IQR
IQR = Q3_math - Q1_math
print(f'IQR для оценок по математике - {IQR}')

# 6. Вычислите стандартное отклонение

Math_std = df["Math"].std()
print(f'\nСтандартное отклонение оценок по математике - {Math_std}')
Chemistry_std = df["Chemistry"].std()
print(f'Стандартное отклонение оценок по химии - {Chemistry_std}')
Russian_std = df["Russian"].std()
print(f'Стандартное отклонение оценок по русскому языку - {Russian_std}')
Literature_std = df["Literature"].std()
print(f'Стандартное отклонение оценок по литературе - {Literature_std}')
English_std = df["English"].std()
print(f'Стандартное отклонение оценок по английскому языку - {English_std}')