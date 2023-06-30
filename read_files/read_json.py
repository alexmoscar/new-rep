import pandas as pd
import json
from pprint import pprint
# Открываем файл и связываем его с объектом "f"
with open('read_files/recipes.json') as f:
    recipes = json.load(f) # Загружаем содержимое открытого файла в переменную recipes
#узнаем к-во ингредиентов в первом блюде
#pprint(len(recipes[0]['ingredients']))
#К какой кухне относится блюдо с id = 13121?
for recipe in recipes:
    if recipe['id']  == 13121:
        print(recipe['cuisine'])
        break
      
#Какое количество уникальных национальных кухонь присутствуют в нашем наборе данных?
cuisines = []
for recipe in recipes:
    if not(recipe['cuisine'] in cuisines):
        cuisines.append(recipe['cuisine'])
#print(len(cuisines))

#СОЗДАНИЕ DATAFRAME ИЗ JSON(ОН ВЫГЛЯДИТ НЕ КАК ТАБЛИЦА, НО МОЖНО ПЕРЕДЕЛАТЬ В НЕЕ)
df = pd.read_json('read_files/recipes.json')
#print(df.info()) # такой вид не очень интересен, так как ингредиенты находятся списком. Нужносделать их по столбцам.
#чтобы это сделать:Создадим функцию для заполнения значения в каждой ячейке.
#Функция будет проверять наличие конкретного ингредиента в столбце ingredients для текущего блюда
#и возвращать 1, если ингредиент есть в рецепте, и 0, если он отсутствует.
all_ingredients = set() # Создаем пустое множество для хранения реестра уникальных ингредиентов
for recipe in recipes: # Начинаем перебор всех блюд входящих в список
    for ingredient in recipe['ingredients']: # Начинаем перебор всех ингредиентов, входящих в состав текущего блюда
        all_ingredients.add(ingredient) # Добавляем уникальный ингредиент в реестр
def contains(ingredient_list): # Определяем имя функции и передаваемые аргументы
    if ingredient_name in ingredient_list: # Если ингредиент есть в текущем блюде,
        return 1 # возвращаем значение 1
    else: # Если ингредиента нет в текущем блюде,
        return 0 # возвращаем значение 0
for ingredient_name in all_ingredients: # Последовательно перебираем ингредиенты в реестре all_ingredients
    # В DataFrame cоздаем столбец с именем текущего ингредиента и заполняем его единицами и нулями
    df[ingredient_name] = df['ingredients'].apply(contains)
df['ingredients'] = df['ingredients'].apply(len) # Заменяем список ингредиентов в рецепте на их количество 
df.to_csv('read_files/recipes.csv', index = False)
