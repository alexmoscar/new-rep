import pandas as pd
countries_data = pd.read_csv('read_files/countries.csv', sep=';')
# Выгружаем данные из DataFrame в CSV-файл и сохраняем файл в папке data
countries_data.to_csv('read_files/countries.txt', index=False, sep=' ')
#Считаем данные из файла countries.txt в переменную txt_df  (объект DataFrame),
# применив функцию read_table() с параметрами sep=' '  и  index_col=['country']
# (так мы избавимся от столбца с индексом и присвоим названия строкам, используя данные одного из столбцов)
txt_df = pd.read_table('read_files/countries.txt', sep=' ', index_col=['country'], header = None)
print(txt_df)