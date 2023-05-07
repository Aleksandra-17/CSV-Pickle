import pandas


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