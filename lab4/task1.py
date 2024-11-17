# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    # Открываем CSV файл и читаем его содержимое
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csvfile:
        # Используем DictReader для чтения CSV файла
        reader = csv.DictReader(csvfile, delimiter=",")

        # Преобразуем данные в список словарей
        json_data = [OrderedDict(row) for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_output)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
