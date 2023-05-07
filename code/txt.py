def save_table_txt(data):
  with open('load_table.csv', 'r') as csv_file, open('save_table.txt',
                                                     'w') as txt_file:
    data = csv_file.read()
    txt_file.write(data)


data = 0
data = save_table_txt(data)