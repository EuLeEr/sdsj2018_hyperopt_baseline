# Sberbank Data Science Journey 2018: Hyperopt Baseline

Бейзлайн к соревнованию [SDSJ 2018 AutoML](http://sdsj.sberbank.ai/): оптимизация параметров lightgbm с помощью [hyperopt](https://github.com/hyperopt/hyperopt).

Перебор параметров осуществляется в рамках заданного для данного датасета лимита времени: если лимит исчерпан, перебор прекращается.


Настройки в файле train.py:
- HYPEROPT_NUM_ITERATIONS - максимальное количество итераций (если позволяет лимит времени)
- HYPEROPT_MAX_TRAIN_SIZE - максимальный размер данных для перебора параметров в Мб
- HYPEROPT_MAX_TRAIN_ROWS - максимальное количество строк в данных для перебора гиперпараметров

---

Для успешной работы с большими датасетами сначала загружается небольшая часть данных, чтобы получить типы колонок, после чего все данные загружаются с числовыми колонками в формате float32 вместо float64. Также колонки, содержащие дату и время, парсятся сразу при загрузке (datetime тип занимает меньше места, чем строка).

---

В файле validate.py тестирование на локальных датасетах на основе бейзлайна https://github.com/vlarine/sdsj2018_lightgbm_baseline, но с добавлением логирования экспериментов с помощью [mlflow](https://mlflow.org/).
mlflow позволяет сохранять параметры, результаты и исходный код экспериментов, смотреть и сравнивать результаты в веб-интерфейсе. Подробнее
https://mlflow.org/docs/latest/tutorial.html
