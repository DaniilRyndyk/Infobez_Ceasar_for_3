import requests
import json


def generate_frequency_dict_and_write_to_file():
    write_dict_to_file(generate_frequency_dict())


def write_dict_to_file(d: dict):
    with open('freq.json', 'w', encoding='UTF-8') as file:
        json.dump(d, file, ensure_ascii=False)


def generate_frequency_dict(txt: str = None) -> dict:
    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'

    if txt is None:
        response = requests.get('http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml')
        txt = response.text

    arr = [i.lower() for i in txt if i.lower() in alphabet]

    d: dict = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1

    return d


def generate_list_for_frequency_analyse(d: dict = None):
    if d is None:
        with open('freq.json', encoding='UTF-8') as file:
            d = json.load(file)

    return [element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    generate_frequency_dict_and_write_to_file()
