import pandas as pd
#countries_data = pd.read_csv('read_files/countries.csv', sep=';')
# Выгружаем данные из DataFrame в CSV-файл и сохраняем файл в папке data
#countries_data.to_csv('read_files/countries.txt', index=False, sep=' ')
#Считаем данные из файла countries.txt в переменную txt_df  (объект DataFrame),
# применив функцию read_table() с параметрами sep=' '  и  index_col=['country']
# (так мы избавимся от столбца с индексом и присвоим названия строкам, используя данные одного из столбцов)
#txt_df = pd.read_table('read_files/countries.txt', sep=' ', index_col=['country'], header = None)


# ОБЯЗАТЕЛЬНО УСТАНОВИТЬ РАСШИРЕНИЕ pip install chardet ДЛЯ ТОГО, ЧТОБЫ УЗНАТЬ КАКАЯ КОДИРОВКА В ФАЙЛЕ

# Считываем данные из файла с неизвестной кодировкой в переменную, создавая объект DataFramedisplay(data)
data=pd.read_csv('read_files/ErrorEnCoding.csv', header=None, encoding_errors='replace')
#               КОД ДЛЯ ОПРЕДЕНИЯ КОДИРОВКИ В ФАЙЛЕ
from chardet.universaldetector import UniversalDetector # Импортируем субмодуль chardet.universaldetectordetector = UniversalDetector()
with open('read_files/ErrorEnCoding.csv', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
detector.close()
