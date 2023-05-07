import pandas
import pickle


print('Вывод данных с помощью csv:')
print()


def load_table_csv(data):
  data = pandas.read_csv('load_table.csv')
  data.head()
  print(data)


data = 0
data = load_table_csv(data)
print()


def save_table_csv(data):
  data = pandas.read_csv('load_table.csv')
  data = data.to_csv('save_table.csv')


data = 0
data = save_table_csv(data)

print('Вывод данных с помощью pickle:')
print()


def load_and_save_table_pickle(data):
  tab_dat = pandas.read_csv('load_table.csv')
  tab_dat.head()

  tab_dat.to_pickle('load_table.pkl')

  with open("load_table.pkl", "rb") as pickle_file:
    data1 = pickle.load(pickle_file)
    print(data1)


data1 = 0
data1 = load_and_save_table_pickle(data)


def save_table_txt(data):
  with open('load_table.csv', 'r') as csv_file, open('save_table.txt',
                                                     'w') as txt_file:
    data = csv_file.read()
    txt_file.write(data)


data = 0
data = save_table_txt(data)
print()
print('Функция get_rows_by_number:')
print()


def get_rows_by_number(start, stop, copy_table):
  file = r'load_table.csv'

  if copy_table == True:
    print('Error!')

  elif copy_table == False:
    table = pandas.read_csv(file)
    print(table[start:stop + 1])


get_rows_by_number(start=0, stop=2, copy_table=False)

print()
print('Функция get_rows_by_index:')
print()


def get_rows_by_index(copy_table):
  if copy_table == False:
    data = pandas.read_csv("get_rows_by_index.csv")
    data['Department'] = data['Department'].replace({
      'Sales': 'London',
      'Depot': 'Boston',
      'Engineering': 'Georgia',
      'History': 'Washington',
      'HR': 'Brussels'
    })
    print(data)
  elif copy_table == True:
    print('Error!')


get_rows_by_index(copy_table=False)
print()
print('Функция get_column_types:')
print()


def get_column_types(by_number):
  file = 'load_table.csv'
  if by_number == True:
    data = pandas.read_csv(file)
    data1 = data.info(memory_usage=False, show_counts=False)
    print(data1)
  if by_number == False:
    print('Error!')


get_column_types(by_number=True)
print()
print('Функция set_column_types:')
print()


def set_column_types(by_number):
  file = r'load_table.csv'
  data = pandas.read_csv(file)
  types_dict = input()
  if by_number == True:
    if types_dict == 'int':
      column_index = data.select_dtypes(include=['int64'])
      print(column_index.info(show_counts=False, memory_usage=False))
    elif types_dict == 'float':
      column_index = data.select_dtypes(include=['float64'])
      print(column_index.info(show_counts=False, memory_usage=False))
    elif types_dict == 'bool':
      column_index = data.select_dtypes(include=['bool'])
      print(column_index.info(show_counts=False, memory_usage=False))
    elif types_dict == 'str':
      column_index = data.select_dtypes(include=['object'])
      print(column_index.info(show_counts=False, memory_usage=False))
    else:
      print('Введите тип данных корректно!')
  elif by_number == False:
    print('Error!')


set_column_types(by_number=True)
print()
print('Функция get_values:')
print()


def get_values(condition, column):
  file = r'load_table.csv'
  data = pandas.read_csv(file)
  if condition == True:
    if type(column) == str:
      print(data[column])
    elif type(column) == int:
      column_index = data.columns[column]
      print(data[column_index])
  elif condition == False:
    print('Error!')
get_values(condition = True, column=0)
print()
print('Функция get_value:')
print()


def get_value(condition, column):
  file = r'table.csv'
  data = pandas.read_csv(file)
  if condition == True:
    if type(column) == str:
      print(data[column])
    elif type(column) == int:
      column_index = data.columns[column]
      print(data[column_index])
  elif condition == False:
    print('Error!')
get_value(condition = True, column = 2)
print()
print('Функция set_values:')
print()


def set_values(condition, column, values):
    file = r'load_table.csv'
    data = pandas.read_csv(file)
    if condition == True:
      if type(column) == str:
        data.loc[:, column] = values
        print(data)
      elif type(column) == int:
        data[data.columns[1]] = values
        print(data)
    elif condition == False:
      print('Error!')
set_values(condition = True, column = 2, values = 1)
print()
print('Функция set_value:')
print()


def set_value(condition, column, value):
    file = r'table.csv'
    data = pandas.read_csv(file)
    if condition == True:
      if type(column) == str:
        data.loc[:, column] = value
        print(data)
      elif type(column) == int:
        data[data.columns[2]] = value
        print(data)
    elif condition == False:
      print('Error!')
set_value(condition = True, column = 2, value = 1)  
print()
print('Функция print_table:')
print()


def print_table(condition):
  if condition == True:
    file = r'load_table.csv'
    data = pandas.read_csv(file)
    print(data)
  elif condition == False:
    print('Error!')
print_table(condition = True)
print()
print('Функция load_tables:')
print()


def load_tables(condition):
  if condition == True:
    data = pandas.concat(map(pandas.read_csv, ['table.csv', 'load_table.csv']))
    print(data)
  elif condition == False:
    print('Error!')
load_tables(condition = True)
print()


def save_tables(condition):
  if condition == True:
    data = pandas.concat(map(pandas.read_csv, ['table.csv', 'load_table.csv']))
    data.to_csv('save_tables.csv')
  elif condition == False:
    print('Error!')
save_tables(condition = True)
print('Функция concat:')
print()


def concat(condition):
  if condition == True:
    data = pandas.concat(map(pandas.read_csv, ['table.csv', 'load_table.csv']))
    print(data)
  elif condition == False:
    print('Error!')
concat(condition = True)