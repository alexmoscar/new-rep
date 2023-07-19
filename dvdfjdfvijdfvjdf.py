input_string = input('Введите число словами: ')
number_word_dict = {
    "ты": 1000, "м": 1000000,
    "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
    "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
    "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
    "деc": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }

def transform_string_to_integer(input_string):
    words = input_string.split()
    number = 0
    for word in words:
        keys = list(number_word_dict.keys())
        filtered_key = list(filter(lambda key : word.startswith(key), keys))[0]
        number += number_word_dict[filtered_key]
    return number
print(transform_string_to_integer(input_string))

            