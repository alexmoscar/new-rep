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
print(len(cuisines))

#Какой из национальных кухонь принадлежит самое большое количество рецептов?
cuisines_name = []
