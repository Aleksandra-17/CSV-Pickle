import pandas
import pickle


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