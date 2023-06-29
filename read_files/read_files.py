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
from chardet.universaldetector import UniversalDetector 
detector = UniversalDetector()
with open('read_files/ErrorEnCoding.csv', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
#print(detector.close()) # узнали, что кодировка - KOI8-R
 # Создаем DataFrame из файла, явно указав кодировку символов, и выводим его содержимое на экран
data=pd.read_csv('read_files/ErrorEnCoding.csv', encoding='koi8-r', header=None )
#print(data)

                #ЧТЕНИЕ ФАЙЛА ПО ССЫЛКЕ   ОБЯЗАТЕЛЬНО УСТАНОВИТЬ PIP INSTALL REQUESTS (ИНОГДА НУЖНО ПЕРЕЗАГРУЗИТЬ)
data = pd.read_table('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv', sep=',')
#print(data)

                #ЧТЕНИЕ ФАЛОВ В ZIP АРХИВЕ
data = pd.read_csv('read_files/students_performance.zip')
#print(data)

                #Запись файла в zip папку
compression_opts = dict(method='zip', archive_name='out.csv')
data.to_csv('data/out.zip', index=False, compression=compression_opts) #data - папка в кот сохр файл
#print(data)

                #РАБОТА С ФАЙЛАМИ EXCEL (УСТАНОВИТЬ PIP INSTALL OPENPYXL)
                        #ЧТЕНИЕ ФАЙЛА XLS,XLSX
grades = pd.read_excel('read_files/grades.xlsx')
#print(grades)

                        #ЧТЕНИЕ EXCEL ПО ССЫЛКЕ
data = pd.read_excel('https://github.com/asaydn/test/raw/master/january.xlsx')
#print(data)

                        # КАК ПРОЧИТАТЬ ОДИН КАКОЙ-ТО ЛИСТ В EXCEL, ЕСЛИ ИХ ТАМ НЕСКОЛЬКО
grades = pd.read_excel('read_files/grades.xlsx', sheet_name='Maths')
print(grades.head(5))
