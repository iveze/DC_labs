import json

INPUT_FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    total_sum = 0.0

    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)  # Загружаем данные из файла

        # Проходим по каждому словарю в списке
        for item in data:
            if 'score' in item and 'weight' in item:  # Проверяем наличие ключей
                total_sum += item['score'] * item['weight']

    return round(total_sum, 3)


print(task())
