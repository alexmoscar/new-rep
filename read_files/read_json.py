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
      
