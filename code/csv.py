import pandas


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